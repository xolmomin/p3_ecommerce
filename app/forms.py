from django.contrib.auth import authenticate
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.db.transaction import atomic
from django.forms import Form, ModelForm, CharField, EmailField
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from jwt.utils import force_bytes

from app.models import Product, User
from app.token import account_activation_token
from p3_ecommerce.settings import EMAIL_HOST_USER


class ProductForm(Form):
    email = EmailField(max_length=255)
    # password = CharField(max_length=255, widget=PasswordInput())
    description = CharField(max_length=255)
    amount = CharField(max_length=255)


class ProductModelForm(ModelForm):
    class Meta:
        model = Product
        # fields = ['title', 'price']
        exclude = ()


class UserForm(Form):
    full_name = CharField()
    email = EmailField()
    address = CharField()


# botir@mail.ru


class UserModelForm(ModelForm):
    class Meta:
        model = User
        exclude = ()


class LoginForm(AuthenticationForm):
    username = CharField(required=False)
    email = EmailField()
    password = CharField(max_length=255)

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError('Bunday email yoq')
        return email

    def clean_password(self):
        email = self.data.get('email')
        password = self.data.get('password')

        user = User.objects.get(email=email)
        if not user.check_password(password):
            raise ValidationError('Parol xato')
        return password

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(
                self.request, email=email, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class RegisterForm(Form):
    username = CharField(max_length=255)
    email = EmailField()
    password = CharField(max_length=255)
    confirm_password = CharField(max_length=255)

    def clean_email(self):
        email = self.data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Bunday email mavjud')
        return email

    def clean_username(self):
        username = self.data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Bunday username mavjud')
        return username

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('tasdiqlash paroli xato')
        return password

    @atomic
    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data.get('username'),
            email=self.cleaned_data.get('email'),
            is_active=False
        )
        user.set_password(self.cleaned_data.get('password'))
        user.save()


class ForgotPasswordForm(Form):
    email = EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError('This profile is not registered')
        return email


def send_email(email, domain, _type):

    user = User.objects.get(email=email)
    subject = 'Activate your account'
    message = render_to_string('app/auth/activation-account.html', {
        'user': user,
        'domain': domain,
        'uid': urlsafe_base64_encode(force_bytes(str(user.pk))),
        'token': account_activation_token.make_token(user),
    })

    from_email = EMAIL_HOST_USER
    recipient_list = [email]

    result = send_mail(subject, message, from_email, recipient_list)
    print('Send to MAIL')

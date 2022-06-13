from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.db.transaction import atomic
from django.forms import Form, ModelForm, CharField, EmailField

from app.models import Product, User


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
            raise ValidationError('Tasdiqlash paroli xato')
        return password

    @atomic
    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data.get('username'),
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('password'),
        )
        user.set_password(self.cleaned_data.get('password'))
        user.save()

class LoginForm(Form):
    email = EmailField()
    password = CharField(max_length=255)

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError('Bunday email yoq')
        return email

    def clean_password(self):
        email = self.cleaned_data.get('email')
        if email:
            password = self.data.get('password')

            user = User.objects.get(email=email)
            if not user.check_password(password):
                raise ValidationError('Parol xato')
            return password


class UserModelForm(ModelForm):
    class Meta:
        model = User
        exclude = ()

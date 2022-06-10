from django.core.exceptions import ValidationError
from django.forms import Form, ModelForm, forms, CharField, EmailField, PasswordInput

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
# botir@mail.ru

class LoginForm(Form):
    email = EmailField()
    password = CharField(max_length=255)

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError('Bunday email yoq')
        return email


class UserModelForm(ModelForm):
    class Meta:
        model = User
        exclude = ()

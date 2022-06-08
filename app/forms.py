from django.forms import Form, ModelForm, forms, CharField, EmailField, PasswordInput

from app.models import Product,Customer


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


class CustomerForm(Form):
    full_name = CharField()
    email = EmailField()
    address = CharField()

class CustomerModelForm(ModelForm):
     class Meta:
        model = Customer
        exclude = ()




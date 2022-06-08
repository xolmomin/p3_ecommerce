from django.core.validators import integer_validator
from django.db.models import (
    FloatField, CharField, IntegerField, Model, ImageField, CASCADE, ForeignKey, EmailField, DateTimeField, SlugField,
    SET_NULL)


# def check_phone_number(phone):
#     if not phone.isdigit():
#         raise ValidationError('Only number')
from django.utils.text import slugify


class BaseModel(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    title = CharField(max_length=255)
    category = ForeignKey('app.Category', SET_NULL, blank=True, null=True)
    price = FloatField()
    description = CharField(max_length=1000, blank=True, null=True)
    amount = IntegerField(default=1)


class Image(Model):
    image = ImageField(upload_to='products/')
    product = ForeignKey('app.Product', CASCADE)


class Customer(BaseModel):
    full_name = CharField(max_length=255, null=True)
    email = EmailField(max_length=255, null=True)
    phone_number = CharField(max_length=25, validators=[integer_validator])
    address = CharField(max_length=255, null=True)


class Category(Model):
    image = ImageField(upload_to='category/')
    name = CharField(max_length=255)
    slug = SlugField()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(force_insert, force_update, using, update_fields)


class Profile(Model):
    first_name = CharField(max_length=255, null=True)
    last_name = CharField(max_length=255, null=True)
    email = EmailField(max_length=255, null=True)
    heading = CharField(max_length=100, null=True)
    intro = CharField(max_length=500, null=True)


"""
ForeignKey
ManyToManyField
OneToOneField

1-n
n-1
n-n
1-1
"""

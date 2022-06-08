from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from app.forms import ProductModelForm, CustomerModelForm
from app.models import *


def add_product(request):
    form = ProductModelForm()

    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'app/add-product.html', context)


def index(request):
    products = Product.objects.all()
    # print(products.query)
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 3)  # 5 users per page

    try:
        pagin = paginator.page(page)
    except:
        pagin = paginator.page(1)
    context = {
        'products': pagin
    }
    return render(request, 'app/index.html', context)


# Product_detals
def product_details(request, product_id):
    # [1, 2, 3]  Product.objects.all()
    # [1]  Product.objects.filter(id=product_id)
    # 1 Product.objects.filter(id=product_id).first()
    product = Product.objects.filter(id=product_id).first()
    context = {
        'product': product
    }
    return render(request, 'app/product_details.html', context)


# Product delete
def product_delete(request):
    return render(request, 'app/index.html')


def profiles(request):
    profile = Profile.objects.all()

    context = {
        'profiles': profile
    }
    return render(request, 'app/profiles.html', context)


# order_list
def order_list(request):
    return render(request, 'app/order_list.html')


# order_list
def order_details(request):
    return render(request, 'app/order_details.html')


def list_users(request):
    page = request.GET.get('page', 1)
    products = Product.objects.all()
    paginator = Paginator(products, 3)  # 5 users per page

    try:
        users = paginator.page(page)
    except:
        users = paginator.page(1)


# customers
def customers(request):
    customer = Customer.objects.all()

    context = {
        'customers': customer
    }

    return render(request, 'app/customers.html', context)


def category(request):
    context = {}
    return render(request, 'app/category.html', context)


def customer_details(request, customer_id):
    customer = Customer.objects.filter(id=customer_id).first()
    print(customer)
    context = {
        'customer': customer
    }
    return render(request, 'app/customer-details.html', context)


def customer_delete(request, customer_id):
    customer = Customer.objects.filter(id=customer_id).first()
    if customer:
        customer.delete()
    return redirect('customers')


def customer_update(request, customer_id):
    customer = Customer.objects.filter(id=customer_id).first()
    form = CustomerModelForm(instance=customer)
    if request.method == 'POST':
        form = CustomerModelForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
        return redirect('customers')

    context = {
        'form': form,
        'action': 'Edit'
    }
    return render(request, 'app/update-customer.html', context)


def customer_add(request):
    form = CustomerModelForm()

    if request.method == 'POST':
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('customers')

    context = {
        'form': form,
        'action': 'Add'
    }
    return render(request, 'app/add-customer.html', context)

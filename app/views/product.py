from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from app.forms import ProductModelForm
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


def index(request, category_slug=None):
    if category_slug:
        products = Product.objects.filter(category__slug=category_slug)
    else:
        products = Product.objects.all()

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

    context = {
        'users': users
    }
    return render(request, 'app/index.html', context)


def category(request):
    categories = Category.objects.filter(parent__isnull=True)
    product_count = Product.objects.filter(category_id__in=categories.values_list('id', flat=True)).count()
    context = {
        'categories': categories,
        'product_count': product_count
    }
    return render(request, 'app/category.html', context)

from django.shortcuts import render, redirect

from app.forms import UserModelForm
from app.models import User


def customers(request):
    customer = User.objects.all()

    context = {
        'customers': customer
    }

    return render(request, 'app/customers.html', context)


def customer_details(request, customer_id):
    customer = User.objects.filter(id=customer_id).first()
    print(customer)
    context = {
        'customer': customer
    }
    return render(request, 'app/customer-details.html', context)


def customer_delete(request, customer_id):
    customer = User.objects.filter(id=customer_id).first()
    if customer:
        customer.delete()
    return redirect('customers')


def customer_update(request, customer_id):
    customer = User.objects.filter(id=customer_id).first()
    form = UserModelForm(instance=customer)
    if request.method == 'POST':
        form = UserModelForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
        return redirect('customers')

    context = {
        'form': form,
        'action': 'Edit'
    }
    return render(request, 'app/update-customer.html', context)


def customer_add(request):
    form = UserModelForm()

    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('customers')

    context = {
        'form': form,
        'action': 'Add'
    }
    return render(request, 'app/add-customer.html', context)

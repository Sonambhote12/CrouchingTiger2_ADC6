from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer

# Create your views here.

def customer_list(request):
    context = {'customer_list':Customer.objects.all()}
    return render(request,"customization/customer_list.html", context)


def customer_form(request,id=0):
    if request.method =="GET":
        if id == 0:
            form = CustomerForm()
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(instance=customer)
        return render(request, "customization/customer_form.html", {'form': form})
    else:
        if id ==0:
            form = CustomerForm(request.POST)
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(request.POST,instance= customer)
        if form.is_valid():
            form.save()
        return redirect('/customer/list') 
           
def customer_delete(request,id):
    customer= Customer.objects.get(pk=id)
    customer.delete()
    return redirect('/customer/list')

    
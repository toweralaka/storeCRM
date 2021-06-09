from django.shortcuts import render
from store.models import Order
from store.models import ShippingAddress
from store.models import OrderItem
# Create your views here.


def orders(request):
    order = Order.objects.all()
    item = OrderItem.objects.all()
    address = ShippingAddress.objects.all()
    context = {'order':order, 'address': address, 'item':item}
    return render(request, 'CRM/orders.html', context)
from django.shortcuts import render
from store.models import Stock

def dashboard_view(request):
    return render (request,'dashboard.html')

def products_all_view(request):
    products = Stock.objects.all()
    return render (request,'products.html',{'products':products})

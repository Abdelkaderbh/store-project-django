from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from store.models import Stock

@login_required
def dashboard_view(request):
    return render (request,'dashboard.html')

@login_required
def products_all_view(request):
    products = Stock.objects.all()
    return render (request,'products.html',{'products':products})

@login_required
def product_detail_view(request,product_id):
    product = Stock.objects.get(id=product_id)
    return render (request,'product_detail.html',{'product':product})
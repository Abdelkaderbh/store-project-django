from django.shortcuts import render,get_object_or_404,redirect
from store.Forms import ProductForm
from store.models import Stock

def dashboard_view(request):
    return render (request,'dashboard.html')

def products_all_view(request):
    products = Stock.objects.all()
    return render (request,'products.html',{'products':products})

def delete_product_view(request,id):
    product = get_object_or_404(Stock,id=id)
    if request.method == "POST":
        product.delete()
        return redirect ('products')
    

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products')
    else:
        form=ProductForm()
        
    return render(request,'add.html',{'form':form})

    
def edit_product(request, id):
    product = get_object_or_404(Stock, id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products') 
    else:
        form = ProductForm(instance=product)  
    
    return render(request, 'update_product.html', {'form': form})

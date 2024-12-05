from django.shortcuts import render,get_object_or_404,redirect
from store.models import Stock
from django.shortcuts import render, get_object_or_404, redirect
from .models import Categorie, Fournisseur,Stock
from .Forms import CategorieForm, FournisseurForm,ProductForm

def dashboard_view(request):
    total_products = Stock.objects.all().count()
    total_categories = Categorie.objects.all().count()
    total_suppliers = Fournisseur.objects.all().count()
    return render (request,'dashboard.html',{'supps':total_suppliers,'categs':total_categories,'products':total_products})

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




def category_list(request):
    categories = Categorie.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})

def category_add(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategorieForm()
    return render(request, 'categories/category_add.html', {'form': form})

def category_edit(request, pk):
    category = get_object_or_404(Categorie, pk=pk)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategorieForm(instance=category)
    return render(request, 'categories/category_edit.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Categorie, pk=pk)
    category.delete()
    return redirect('category_list')


def supplier_list(request):
    suppliers = Fournisseur.objects.all()
    return render(request, 'suppliers/supplier_list.html', {'suppliers': suppliers})

def supplier_add(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('supplier_list')  
    else:
        form = FournisseurForm()  
    return render(request, 'suppliers/supplier_add.html', {'form': form})

def supplier_edit(request, pk):
    supplier = get_object_or_404(Fournisseur, pk=pk)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = FournisseurForm(instance=supplier)
    return render(request, 'suppliers/supplier_edit.html', {'form': form, 'supplier': supplier})

def supplier_delete(request, pk):
    supplier = get_object_or_404(Fournisseur, pk=pk)
    supplier.delete()
    return redirect('supplier_list')


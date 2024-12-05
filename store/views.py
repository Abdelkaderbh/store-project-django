from django.contrib.auth.decorators import login_required
from store.models import Stock
from django.shortcuts import render, get_object_or_404, redirect
from .models import Categorie, Fournisseur,Stock
from .forms import CategorieForm, FournisseurForm,ProductForm

@login_required
def dashboard_view(request):
    total_products = Stock.objects.all().count()
    total_categories = Categorie.objects.all().count()
    total_suppliers = Fournisseur.objects.all().count()
    return render (request,'dashboard.html',{'supps':total_suppliers,'categs':total_categories,'products':total_products, 'current_page': 'Dashboard'})

@login_required
def products_all_view(request):
    products = Stock.objects.all()
    return render (request,'products.html',{'products':products, 'current_page': 'Products'})

@login_required
def product_detail_view(request,product_id):
    product = Stock.objects.get(id=product_id)
    return render (request,'product_detail.html',{'product':product})
  
@login_required
def delete_product_view(request,id):
    product = get_object_or_404(Stock,id=id)
    if request.method == "POST":
        product.delete()
        return redirect ('products')
    
@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products')
    else:
        form=ProductForm()
        
    return render(request,'add.html',{'form':form})

@login_required   
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

@login_required
def category_list(request):
    categories = Categorie.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories, 'current_page': 'Categories'})
  
@login_required
def category_add(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategorieForm()
    return render(request, 'categories/category_add.html', {'form': form})

@login_required
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

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Categorie, pk=pk)
    category.delete()
    return redirect('category_list')

@login_required
def supplier_list(request):
    suppliers = Fournisseur.objects.all()
    return render(request, 'suppliers/supplier_list.html', {'suppliers': suppliers, 'current_page': 'Suppliers'})

@login_required
def supplier_add(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('supplier_list')  
    else:
        form = FournisseurForm()  
    return render(request, 'suppliers/supplier_add.html', {'form': form})

@login_required
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

@login_required
def supplier_delete(request, pk):
    supplier = get_object_or_404(Fournisseur, pk=pk)
    supplier.delete()
    return redirect('supplier_list')



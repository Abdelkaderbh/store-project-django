from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('products/',views.products_all_view,name='products'),
    path('product/delete/<int:id>/', views.delete_product_view, name='delete_product'),
    path('product/edit/<int:id>/',views.edit_product,name='edit_product'),
    path('product/add',views.add_product,name='add_product'),

    # Categories
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_add, name='category_add'),
    path('categories/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),

    # Suppliers
    path('Suppliers/', views.supplier_list, name='supplier_list'),
    path('Suppliers/add/', views.supplier_add, name='supplier_add'),
    path('Suppliers/edit/<int:pk>/', views.supplier_edit, name='supplier_edit'),
    path('Suppliers/delete/<int:pk>/', views.supplier_delete, name='supplier_delete'),
]

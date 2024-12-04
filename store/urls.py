from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('products/',views.products_all_view,name='products'),
    path('product/delete/<int:id>/', views.delete_product_view, name='delete_product'),
    path('product/edit/<int:id>/',views.edit_product,name='edit_product'),
    path('product/add',views.add_product,name='add_product')
]

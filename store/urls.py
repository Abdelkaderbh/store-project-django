from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('products/',views.products_all_view,name='products')
]

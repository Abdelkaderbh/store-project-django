
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('dashboard/', permanent=False)),
    path('',include('store.urls')),
    path('accounts/',include('accounts.urls'))
]

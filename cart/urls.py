"""
URL configuration for mymainproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path,include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include('accounts.urls')),
#     path('',include('cart.urls')),
#     path('',include('products.urls')),
#
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),

    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('increase/<int:cart_id>/', views.increase_quantity, name='increase_quantity'),

    path('decrease/<int:cart_id>/', views.decrease_quantity, name='decrease_quantity'),

    path('remove/<int:cart_id>/', views.remove_cart, name='remove_cart'),
]
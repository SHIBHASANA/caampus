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
    path('', views.home, name='home'),

    path(
        'product/<int:id>/',
        views.product_details,
        name='product_details'
    ),

    path(
        'search/',
        views.search_products,
        name='search_products'
    ),

    path(
        "my-products/",
        views.my_products,
        name="my_products",
    ),
    path(
        'add-product/',
        views.add_product,
        name='add_product'
    ),
    path(
        'edit-product/<int:id>/',
        views.edit_product,
        name='edit_product'
    ),
    path(
        "delete-product/<int:id>/",
        views.delete_product,
        name="delete_product"
    ),
    path(
        "dashboard/",
        views.seller_dashboard,
        name="seller_dashboard"
    ),
]
from django.contrib import admin
from .models import Cart

# @admin.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#     list_display = (
#         'user',
#         'product',
#         'quantity',
#         'created_at'
#     )
#
#     list_filter = (
#         'created_at',
#     )
#
#     search_fields = (
#         'user__username',
#         'product__title'
#     )
#

admin.site.register(Cart)
from django.contrib import admin

# Register your models here.

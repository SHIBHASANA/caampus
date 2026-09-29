from django.contrib import admin
from .models import Category, Product
from .models import Review

admin.site.register(Review)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'price',
        'seller',
        'college',
        'stock',
        'is_available'
    ]


from .models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_active',
        'created_at'
    )

    list_filter = ('is_active',)

    search_fields = ('title',)


from django.contrib import admin

# Register your models here.

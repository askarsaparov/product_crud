from django.contrib import admin

from product.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')
    search_fields = ('title',)
    list_filter = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

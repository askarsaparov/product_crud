from django.urls import path

from product.views.category import listCategory, detailCategory
from product.views.product import listProduct, detailProduct, searchProduct

app_name = 'product'

urlpatterns = [

    # Category
    path('category/', listCategory, name='list-category'),
    path('category/<int:id>/', detailCategory, name='detail-category'),

    # Product
    path('product/', listProduct, name='list-product'),
    path('product/search', searchProduct, name='search-product'),
    path('product/<int:id>/', detailProduct, name='detail-product'),
]

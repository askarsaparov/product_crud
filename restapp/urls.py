from django.urls import path, include

app_name = 'restapp'

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('products/', include('product.urls')),

]

from drf_yasg import openapi
from rest_framework import serializers


class ProductPostSchema(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField(max_length=255)
    category = serializers.IntegerField()
    image = serializers.CharField()


class ProductGetSchema(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField(max_length=255)
    category = serializers.CharField()
    image = serializers.CharField()


search_param = [openapi.Parameter(
    name='search',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    description='Search (title, description, category__title)',
    required=False
)]

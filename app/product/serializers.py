from rest_framework.serializers import ModelSerializer

from product.models import Category, Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title", "description", "image")


class ProductSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ("id", "title", "description", "image", "price", "category")

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['category'] = CategorySerializer(instance.category).data['title']
        return response

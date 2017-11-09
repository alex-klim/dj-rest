from rest_framework.serializers import ModelSerializer
from .models import *

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'category']

class CategorySerializer(ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ['name', 'products']
        many = True


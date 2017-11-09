from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import ProductSerializer, CategorySerializer


class ProductView(ListAPIView, CreateAPIView):
    serializer_class = ProductSerializer
#    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Product.objects.all().filter(category__id=1)

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryView(ListAPIView, CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        prod = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(prod)
        return Response(serializer.data)

class FreshProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


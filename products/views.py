from django.shortcuts import render

# Create your views here.

from django.views.generic.detail import DetailView
from django.views.generic import ListView
from rest_framework import routers, serializers, viewsets


from .models import Product




from rest_framework import viewsets

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name', 'sku', 'link', 'brand')


class ProductViewSet(viewsets.ModelViewSet):
	model = Product
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	filter_fields = ['sku']

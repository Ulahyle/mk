from rest_framework import viewsets
from store.models import Product, Customer
from store.serializers import ProductSerializer, CustomerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .services import check_low_stock

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        product = serializer.save()
        check_low_stock(product)

    def perform_create(self,serializer):
        product=serializer.save()
        check_low_stock(product)
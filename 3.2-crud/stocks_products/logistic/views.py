from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']



class ProductStockViewSet(SearchFilter):
    search_param = 'stock'


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [ProductStockViewSet]
    search_fields = ['address']

from rest_framework.response import Response
from rest_framework import viewsets, status

from .serializers import ProductSerializer,ProductListSerializer
from .models import Product
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductListSerializer

    def create(self, request):
        data_list = request.data
        ser = self.serializer_class(data=data_list, many=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)

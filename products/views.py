from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.permissions import ReadOnly

class ProductModelViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  authentication_classes=[JWTAuthentication]
  permission_classes=[IsAdminUser]

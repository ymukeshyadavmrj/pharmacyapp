from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Favourites
from .serializers import FavouritesSerializer
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from products.models import Product
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def favouritesapi(request, pk=None):
 if request.method == 'GET':
  id = pk
  if id is not None:
   try:
       fav = Favourites.objects.get(product__id=id,user=request.user)
       serializer = FavouritesSerializer(fav)
       return Response(serializer.data)
   except Favourites.DoesNotExist:
       return Response({'isFavourite':False})
  return Response(serializer.data)

 if request.method == 'POST':
  request.data['product']=pk
  request.data['user']=request.user.id
  serializer = FavouritesSerializer(data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 if request.method == 'PATCH':
  fav = Favourites.objects.get(product__id=pk,user=request.user)
  serializer = FavouritesSerializer(fav, data=request.data, partial=True)
  if serializer.is_valid():
   serializer.save()
   return Response({'updateMessage':'Partial Data Updated'})
  return Response(serializer.errors)

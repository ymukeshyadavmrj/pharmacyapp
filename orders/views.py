from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def ordersapi(request, pk=None):
 if request.method == 'GET':
  id = pk
  if id is None:
   ord = Order.objects.get(user=request.user)
   serializer = OrderSerializer(ord)
   return Response(serializer.data)
  return Response({'message':'Dont provide key in for list of orders'})

 if request.method == 'POST':
  request.data['user']=request.user.id
  serializer = OrderSerializer(data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

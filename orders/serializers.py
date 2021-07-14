from rest_framework import serializers
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    #dateTime = serializers.DateField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    class Meta:
        model = Order
        fields = ['id', 'order_status','product','user','quantity']

from django.core.validators import MinValueValidator
from django.db import models
# Create your models here.
from products.models import Product
from django.contrib.auth import get_user_model
User = get_user_model()


class Order(models.Model):
    Ordered = 0
    On_the_way = 1
    Delivered = 2

    ORDER_STATUS = (
        (Ordered, "Ordered"),
        (On_the_way, "On the way"),
        (Delivered, "Delivered"),
    )
    order_status = models.SmallIntegerField(choices=ORDER_STATUS, default=Ordered)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False, related_name='orders_status')
    user = models.ForeignKey(User, related_name='your_orders', on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    dateTime = models.DateField(blank=True, null=True)

from django.db import models
from products.views import Product
from django.contrib.auth import get_user_model
User = get_user_model()

class Favourites(models.Model):
    product = models.ForeignKey(Product, related_name='favourites', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='favourites', on_delete=models.CASCADE)
    isFavourite = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('product', 'user')

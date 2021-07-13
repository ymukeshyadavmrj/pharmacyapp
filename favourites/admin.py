from django.contrib import admin
from .models import Favourites
# Register your models here.

@admin.register(Favourites)
class FavouritesAdmin(admin.ModelAdmin):
 list_display = ['id', 'isFavourite',]

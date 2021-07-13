from rest_framework import serializers
from favourites.models import Favourites


class FavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourites
        fields = ['id', 'isFavourite','product','user']

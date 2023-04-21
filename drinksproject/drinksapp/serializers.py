from rest_framework import serializers
from drinksapp.models import Drink

class DrinkSerializers(serializers.ModelSerializer):

    class Meta:
        model=Drink
        fields='__all__'
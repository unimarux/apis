from rest_framework import serializers
from .models import Category , Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
        depth = 1
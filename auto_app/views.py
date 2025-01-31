from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Food , Category
from .serializers import  FoodSerializer
from django.forms.models import model_to_dict
from rest_framework import generics


class FoodListAPIView(generics.ListCreateAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()



class FoodDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
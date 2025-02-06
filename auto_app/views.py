from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Food
from .serializers import  FoodSerializer
from django.forms.models import model_to_dict
from rest_framework import generics, permissions
from rest_framework import status, viewsets


class FoodsApiView(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
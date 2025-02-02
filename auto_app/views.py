from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Course , Category
from .serializers import  CourseSerializer
from django.forms.models import model_to_dict
from .permissons import IsAdminOrReadOnly
from rest_framework import generics


class CourseListAPIView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAdminOrReadOnly]



class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAdminOrReadOnly]
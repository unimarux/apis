from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Comment , Theme
from .serializers import  CommentSerializer
from django.forms.models import model_to_dict
from rest_framework import generics, permissions


class CommentListAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]



class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

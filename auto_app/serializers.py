from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser

from .models import Book , Comment , Category , MyUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id' , 'title' , 'content' , 'created' , 'category']
        depth = 1
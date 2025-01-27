from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser

from .models import Book , Comment , Category , MyUser

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(required=False)
    created = serializers.DateField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=MyUser.objects.all())

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance:Book, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance
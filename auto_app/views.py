from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Article , Comment , Category
from rest_framework.serializers import Serializer
from django.forms.models import model_to_dict


class HomeApi(APIView , Serializer):
    def get(self , request:Request , pk=None):
        news = Article.objects.all()
        cars_list = []
        if not pk:
            for new in news:
                cars_list.append({
                    'id':new.id,
                    'title':new.title,
                    'category':new.category.name,
                    'author':new.author.username,
                    'created':new.created,
                    'content':new.content,
                })
            return Response({
                'news':cars_list
            })
        else:
            try:
                new = Article.objects.get(pk=pk)
                return Response(
                        model_to_dict(new)
                    )
            except:
                return Response(status=404)

    # def post(self , request:Request):

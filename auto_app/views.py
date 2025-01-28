from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Book , Comment , Category
from django.forms.models import model_to_dict
from .serializers import BookSerializer
from .permissons import BookPermission


class HomeApi(APIView):
    permission_classes = [BookPermission]
    def get(self , request:Request , pk=None):
        books = Book.objects.all()
        if not pk:
            return Response(
                BookSerializer(books, many=True).data
            )
        else:
            try:
                books = Book.objects.get(pk=pk)
                serializer = BookSerializer(books)
                return Response(
                        BookSerializer(books).data
                    )
            except:
                return Response(status=404)

    def post(self, request: Request, pk=None):
        if pk:
            return Response(
                "Method POST is not allowed here",
                status=405
            )
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.create(validated_data=serializer.validated_data)

        return Response(serializer.data)

    def put(self , request:Request , pk=None):
        if not pk:
            return Response(
                "Method PUT is not allowed here",
                status=405
            )

        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance=Book.objects.get(pk=pk),
                          validated_data=request.data)
        return Response(serializer.data)

    def delete(self , request:Request , pk=None):
        if not pk:
            return Response(
                "Method DELETE is not allowed here",
                status=405
            )
        Book.objects.get(pk=pk).delete()
        return Response(status=204)
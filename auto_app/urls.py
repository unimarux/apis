from django.urls import path
from .views import CommentListAPIView , CommentDetailAPIView

urlpatterns = [
    path('api/v1.0/themes', CommentListAPIView.as_view(), name='home'),
    path('api/v1.0/themes/<int:pk>', CommentDetailAPIView.as_view(), name='home'),
]
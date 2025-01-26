from django.urls import path
from .views import HomeApi

urlpatterns = [
    path('api/v1.0/articles', HomeApi.as_view(), name='home'),
    path('api/v1.0/articles/<int:pk>', HomeApi.as_view(), name='home'),
]
from django.urls import path
from .views import HomeApi

urlpatterns = [
    path('', HomeApi.as_view(), name='home'),
    path('api/v1.0/<int:pk>', HomeApi.as_view(), name='home'),
]
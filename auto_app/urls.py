from django.urls import path
from .views import FoodListAPIView , FoodDetailAPIView

urlpatterns = [
    path('api/v1.0/foods', FoodListAPIView.as_view(), name='home'),
    path('api/v1.0/foods/<int:pk>', FoodDetailAPIView.as_view(), name='home'),
]
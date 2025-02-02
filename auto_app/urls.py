from django.urls import path
from .views import CourseListAPIView , CourseDetailAPIView

urlpatterns = [
    path('api/v1.0/courses', CourseListAPIView.as_view(), name='home'),
    path('api/v1.0/courses/<int:pk>', CourseDetailAPIView.as_view(), name='home'),

]
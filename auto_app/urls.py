from django.urls import path , include
from .views import FoodsApiView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', FoodsApiView)


urlpatterns = [
    path("",include(router.urls))
]
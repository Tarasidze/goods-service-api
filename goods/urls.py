from django.urls import path, include
from rest_framework import routers

from goods.views import CategoryViewSet


router = routers.DefaultRouter()

router.register("category", CategoryViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "goods"

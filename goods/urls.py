from django.urls import path, include
from rest_framework import routers

from goods.views import CategoryViewSet, ArticleViewSet


router = routers.DefaultRouter()

router.register("category", CategoryViewSet)
router.register("article", ArticleViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "goods"

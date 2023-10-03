from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet
from goods.models import Article, Category
from goods.serializers import CategorySerializer


class CategoryViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser,)

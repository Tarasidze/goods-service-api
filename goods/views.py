from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAdminUser
from django.db.models.query import QuerySet
from goods.models import Article, Category

from goods.serializers import (
    CategorySerializer,
    ArticleSerializer,
    ArticleListSerializers,
    ArticleDetailSerializer,

)


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


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = (Article.objects.all().select_related("category"))
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self) -> QuerySet:
        """ filtering by Category """
        category_id = self.request.query_params.get("category")
        offer_of_the_month = self.request.query_params.get("offer_of_the_month")
        available = self.request.query_params.get("available")
        self_delivery = self.request.query_params.get("self_delivery")

        queryset = self.queryset

        if category_id:
            queryset = queryset.filter(category__id=int(category_id))

        if offer_of_the_month:
            queryset = queryset.filter(offer_of_the_month=offer_of_the_month)

        if available:
            queryset = queryset.filter(available=available)

        if self_delivery:
            queryset = queryset.filter(self_delivery=self_delivery)

        return queryset

    def get_serializer_class(self):
        """ get serializer depends on request"""
        if self.action == "list":
            return ArticleListSerializers

        if self.action == "retrieve":
            return ArticleDetailSerializer

        return ArticleSerializer

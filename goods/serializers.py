from rest_framework import serializers


from goods.models import Article, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "category_name",)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "name",
            "photo",
            "category",
            "offer_of_the_month",
            "available",
            "self_delivery",
            "description",
            "price",
        )


class ArticleListSerializers(ArticleSerializer):
    category_name = serializers.CharField(
        source="category.category_name", read_only=True
    )

    class Meta:
        model = Article
        fields = ("id", "name", "category_name", "available", "price",)


class ArticleDetailSerializer(ArticleSerializer):
    class Meta:
        model = Article
        fields = (
            "name",
            "photo",
            "category",
            "offer_of_the_month",
            "available",
            "self_delivery",
            "description",
            "price",
        )


class ArticleUpdateSerializer(ArticleSerializer):
    class Meta:
        model = Article
        fields = (
            "name",
            "photo",
            "category",
            "offer_of_the_month",
            "available",
            "self_delivery",
            "description",
            "price",
        )


class ArticleDeleteSerializer(ArticleSerializer):
    class Meta:
        fields = ("id",)

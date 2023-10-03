from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["category_name"]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name


class Article(models.Model):
    name = models.CharField(max_length=63, unique=True)
    photo = models.URLField(max_length=255)
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name="goods"
    )
    offer_of_the_month = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    self_delivery = models.BooleanField(default=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

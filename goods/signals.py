from django.db.models.signals import post_save
from django.dispatch import receiver

from goods.models import Article


@receiver(post_save, sender=Article)
def email_save_article(created, **kwargs):
    if created:
        instance = kwargs["instance"]
        name = instance.name
        category = instance.category
        offer_of_the_month = instance.offer_of_the_month
        available = instance.available

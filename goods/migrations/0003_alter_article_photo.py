# Generated by Django 4.2.5 on 2023-10-03 19:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("goods", "0002_alter_category_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="photo",
            field=models.URLField(max_length=511),
        ),
    ]

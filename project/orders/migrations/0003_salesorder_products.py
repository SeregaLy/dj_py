# Generated by Django 4.1.5 on 2023-01-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
        ("orders", "0002_salesorder_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="salesorder",
            name="products",
            field=models.ManyToManyField(to="products.product"),
        ),
    ]

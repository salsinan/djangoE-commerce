# Generated by Django 4.1 on 2022-09-04 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sales", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sale",
            name="total_price",
            field=models.FloatField(blank=True, null=True),
        ),
    ]

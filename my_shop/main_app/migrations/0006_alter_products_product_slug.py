# Generated by Django 4.1.1 on 2022-09-25 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_products_index_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_slug',
            field=models.CharField(default='___', max_length=100, unique=True, verbose_name='url товара'),
        ),
    ]

# Generated by Django 3.2.6 on 2021-11-09 12:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_market', '0004_car_carproduct'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarProduct',
            new_name='CartProduct',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]

# Generated by Django 3.2.6 on 2021-11-30 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lodging', '0004_auto_20211130_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='lodging',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 3.2.6 on 2021-09-19 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0013_auto_20210918_1232'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'permissions': (('can_publish', 'Может разрешать публиковать'),), 'verbose_name': 'новость', 'verbose_name_plural': 'новости'},
        ),
    ]

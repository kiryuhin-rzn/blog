# Generated by Django 3.2.6 on 2021-11-30 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lodging', '0003_numberrooms_numbers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='numberrooms',
            options={'verbose_name': 'количество комнат', 'verbose_name_plural': 'количество комнат'},
        ),
        migrations.AddField(
            model_name='lodging',
            name='description',
            field=models.TextField(default='', verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='lodging',
            name='published_at',
            field=models.DateTimeField(null=True, verbose_name='дата публикации'),
        ),
    ]
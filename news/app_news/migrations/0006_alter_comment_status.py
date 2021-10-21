# Generated by Django 3.2.6 on 2021-09-02 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0005_alter_comment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('draft', 'Удалено'), ('published', 'Published')], default=None, max_length=10),
        ),
    ]

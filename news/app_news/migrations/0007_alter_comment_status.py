# Generated by Django 3.2.6 on 2021-09-02 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0006_alter_comment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]

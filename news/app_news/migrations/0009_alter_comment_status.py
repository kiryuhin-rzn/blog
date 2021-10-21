# Generated by Django 3.2.6 on 2021-09-02 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0008_alter_comment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], default='d', max_length=10),
        ),
    ]

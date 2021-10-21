# Generated by Django 3.2.6 on 2021-09-18 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0012_auto_20210909_0835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'permissions': (('can_publish', 'Может публиковать'),), 'verbose_name': 'новость', 'verbose_name_plural': 'новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.ManyToManyField(default=None, null=True, to='app_news.Tag'),
        ),
    ]

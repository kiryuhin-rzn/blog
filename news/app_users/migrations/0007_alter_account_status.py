# Generated by Django 3.2.6 on 2021-11-14 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0006_alter_account_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='status',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=10),
        ),
    ]

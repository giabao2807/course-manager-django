# Generated by Django 3.2.8 on 2022-02-20 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_account', '0003_migrate_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
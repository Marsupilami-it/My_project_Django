# Generated by Django 3.1.4 on 2021-01-02 15:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0013_auto_20210102_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 4, 15, 18, 44, 72555, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
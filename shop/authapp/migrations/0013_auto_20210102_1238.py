# Generated by Django 3.1.4 on 2021-01-02 12:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0012_auto_20210102_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 4, 12, 38, 26, 314884, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
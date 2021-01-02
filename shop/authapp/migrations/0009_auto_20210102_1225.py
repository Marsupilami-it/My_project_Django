# Generated by Django 3.1.4 on 2021-01-02 12:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_auto_20201226_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopuserprofile',
            name='about_me',
        ),
        migrations.AddField(
            model_name='shopuserprofile',
            name='aboutMe',
            field=models.TextField(blank=True, max_length=512, verbose_name='о себе'),
        ),
        migrations.AddField(
            model_name='shopuserprofile',
            name='address',
            field=models.TextField(blank=True, max_length=512, verbose_name='адрес'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128, verbose_name='ключ подтверждения'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 4, 12, 25, 25, 41164, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='users_avatars'),
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'М'), ('W', 'Ж')], max_length=1, verbose_name='пол'),
        ),
    ]

# Generated by Django 2.2.16 on 2020-11-12 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='users_avatars', verbose_name='аватар'),
        ),
    ]

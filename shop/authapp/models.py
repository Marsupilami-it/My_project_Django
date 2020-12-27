from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from datetime import timedelta


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField('возраст', default=18)
    avatar = models.ImageField('аватар', upload_to='avatars', blank=True)

    # Ключ идентификации пользователя
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    # Функция проверки срока годности ключа активации
    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        return True

    def basket_total_cost(self):
        return sum(map(lambda x: x.product_cost, self.basket.all()))

    def basket_total_qty(self):
        return sum(map(lambda x: x.quantity, self.basket.all()))

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()
        # доделать
        return 1, {}


# Модель для хранения данных профиля из VK.
class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'W'),
    )

    user = models.OneToOneField(ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(max_length=128, blank=True, verbose_name='теги')
    about_me = models.TextField(blank=True, verbose_name='о себе')
    gender = models.CharField(max_length=1, blank=True, choices=GENDER_CHOICES, verbose_name='пол')


    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()

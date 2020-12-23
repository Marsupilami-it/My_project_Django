from django.db import models


class MotoCategory(models.Model):
    name = models.CharField('категория товара', max_length=64)
    description = models.TextField('описание', blank=True)

    class Meta:
        verbose_name = 'категория товара'
        verbose_name_plural = 'категории товаров'

    def __str__(self):
        return f'Категория {self.name}'


class Moto(models.Model):
    category = models.ForeignKey(MotoCategory, on_delete=models.CASCADE)
    name = models.CharField('имя', max_length=64)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField('описание', blank=True)
    short_desc = models.CharField('краткое описание', max_length=64, blank=True)
    price = models.DecimalField('цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField('количество на складе', default=0)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товар'

    def __str__(self):
        return f'{self.name} ({self.category.name})'

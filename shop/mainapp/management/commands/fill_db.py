import json

from django.core.management.base import BaseCommand

from mainapp.models import Moto, MotoCategory

from authapp.models import ShopUser


def load_from_json(file_name):
    with open(file_name, encoding='utf-8') as infile:
        return json.load(infile)


# Скрипт восстановления данных
class Command(BaseCommand):
    help = 'Fill data in db'

    def handle(self, *args, **options):
        items = load_from_json('mainapp/json/categories.json')
        for item in items:
            MotoCategory.objects.create(**item)

        items = load_from_json('mainapp/json/products.json')
        for item in items:
            category = MotoCategory.objects.filter(name=item['category']).first()
            item['category'] = category
            Moto.objects.create(**item)

    if not ShopUser.objects.filter(username='django').exists():
        ShopUser.objects.create_superuser('django', 'django@gb.local', 'geekbrains')

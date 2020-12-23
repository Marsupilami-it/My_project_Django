from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
import random
from mainapp.models import MotoCategory

from mainapp.models import Moto

from basketapp.models import Basket


def get_catalog_menu():
    return MotoCategory.objects.all()


def get_hot_product():
    products = Moto.objects.all()
    return random.choice(products)


def get_same_products(product):
    return Moto.objects.filter(category=product.category).exclude(pk=product.pk)


def index(request):
    context = {
        'page_title': 'Главная',
        'catalog_menu': get_catalog_menu,
    }
    return render(request, 'mainapp/index.html', context=context)


def products(request):
    hot_product = get_hot_product()

    context = {
        'page_title': 'Каталог',
        'hot_product': hot_product,
        'same_products': get_same_products(hot_product),
        'catalog_menu': get_catalog_menu,
    }
    return render(request, 'mainapp/products.html', context=context)


def category_items(request, category_pk, page_num=1):
    if category_pk == 0:
        products = Moto.objects.all()
    else:
        products = Moto.objects.filter(category_id=category_pk)

    products_paginator = Paginator(products, 2)
    try:
        products = products_paginator.page(page_num)
    except PageNotAnInteger:
        products = products_paginator.page(1)
    except EmptyPage:
        products = products_paginator.page(products_paginator.num_pages)

    context = {
        'page_title': 'Каталог',
        'catalog_menu': get_catalog_menu,
        'products': products,
        'category_pk': category_pk,
    }
    return render(request, 'mainapp/category_items.html', context=context)


def product_page(request, product_pk):
    product = get_object_or_404(Moto, pk=product_pk)

    context = {
        'page_title': 'Продукт',
        'catalog_menu': get_catalog_menu,
        'product': product,
        'category_pk': product.category_id,
    }
    return render(request, 'mainapp/product_page.html', context=context)


def contact(request):
    _locations = [
        {
            'city': 'Москва',
            'phone': '+7-888-888-8888',
            'email': 'shop@gmail.com',
            'address': 'В пределах МКАД',
        },
        {
            'city': 'Екатеринбург',
            'phone': '+7-889-889-8989',
            'email': 'shop@gmail.com',
            'address': 'Центральный проспект',
        },
        {
            'city': 'Казань',
            'phone': '+7-887-878-8778',
            'email': 'shop@gmail.com',
            'address': 'Красная площадь',
        },
    ]

    context = {
        'page_title': 'Контакты',
        'locations': _locations,
        'catalog_menu': get_catalog_menu,
    }
    return render(request, 'mainapp/contact.html', context=context)

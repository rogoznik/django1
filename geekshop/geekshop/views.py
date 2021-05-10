from django.shortcuts import render
from mainapp.models import Product


def main(request):
    products = Product.objects.all()

    context = {
        'slogan': 'Супер пупер СТУЛЬЯ',
        'topic': 'Тренды',
        'title': 'главная',
        'products': products
    }
    return render(request, 'index.html', context=context)


def contacts(request):
    context = {
        'title': 'контакты',
    }
    return render(request, 'contact.html', context=context)

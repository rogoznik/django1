from django.shortcuts import render
from .models import ProductCategory


def products(request):
    product_categories = ProductCategory.objects.all()

    context = {
        'links': [],
        'title': 'товары',
    }

    for cat in product_categories:
        context['links'].append({
            'href': 'products:' + cat.url,
            'name': cat.name,
            'url_name': cat.url
        })

    return render(request, 'products.html', context=context)

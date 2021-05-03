from django.shortcuts import render


def products(request):
    context = {
        'links': [
            {'href': 'products:index', 'name': 'все', 'url_name': 'index'},
            {'href': 'products:home', 'name': 'дом', 'url_name': 'home'},
            {'href': 'products:office', 'name': 'офис', 'url_name': 'office'},
            {'href': 'products:modern', 'name': 'модерн', 'url_name': 'modern'},
            {'href': 'products:classic', 'name': 'классика', 'url_name': 'classic'}
        ],
        'title': 'товары',
    }
    return render(request, 'products.html', context=context)

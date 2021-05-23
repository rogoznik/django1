from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

from mainapp.models import Product, ProductCategory
from authapp.models import ShopUser
from .forms import ShopUserEditForm, ShopUserCreateForm
from .forms import ProductCategoryEditForm, ProductCategoryCreateForm
from .forms import ProductCreateForm, ProductEditForm


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return HttpResponseRedirect(reverse('adminapp:categories'))


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'админка/пользователи/создание'

    if request.method == 'POST':
        create_form = ShopUserCreateForm(request.POST, request.FILES)
        if create_form.is_valid():
            create_form.save()
            return HttpResponseRedirect(reverse('adminapp:users'))
    else:
        create_form = ShopUserCreateForm()

    content = {'title': title, 'create_form': create_form}

    return render(request, 'adminapp/user_create.html', context=content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'админка/пользователи/редактирование'

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:user_update', args=[user.pk]))
    else:
        edit_form = ShopUserEditForm(instance=user)

    content = {'title': title, 'edit_form': edit_form}

    return render(request, 'adminapp/user_edit.html', context=content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'админка/пользователи/удаление'

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('adminapp:users'))

    content = {'title': title, 'user_to_delete': user}

    return render(request, 'adminapp/user_delete.html', content)


def categories(request):
    title = 'админка/категории'

    categories_list = ProductCategory.objects.all()

    context = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', context)


def category_create(request):
    title = 'админка/категории/создание'

    if request.method == 'POST':
        create_form = ProductCategoryCreateForm(request.POST, request.FILES)
        if create_form.is_valid():
            create_form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
    else:
        create_form = ProductCategoryCreateForm()

    content = {'title': title, 'create_form': create_form}

    return render(request, 'adminapp/category_create.html', context=content)


def category_update(request, pk):
    title = 'админка/категории/редактирование'

    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:category_update', args=[category.pk]))
    else:
        edit_form = ProductCategoryEditForm(instance=category)

    content = {'title': title, 'edit_form': edit_form, 'category_to_update': category}

    return render(request, 'adminapp/category_edit.html', context=content)


def category_delete(request, pk):
    title = 'админка/пользователи/удаление'

    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('adminapp:categories'))

    content = {'title': title, 'category_to_delete': category}

    return render(request, 'adminapp/category_delete.html', content)


def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', context)


def product_create(request, pk):
    title = 'админка/продукты/создание'

    if request.method == 'POST':
        create_form = ProductCreateForm(request.POST, request.FILES)
        if create_form.is_valid():
            new_product = create_form.save(commit=False)
            new_product.category_id = pk
            new_product.save()
            return HttpResponseRedirect(reverse('adminapp:products', args=[pk]))
    else:
        create_form = ProductCreateForm()

    content = {'title': title, 'create_form': create_form, 'category_pk': pk}

    return render(request, 'adminapp/product_create.html', context=content)


def product_read(request, pk):
    pass


def product_update(request, pk):
    title = 'админка/продукты/редактирование'

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:product_update', args=[product.pk]))
    else:
        edit_form = ProductEditForm(instance=product)

    content = {'title': title, 'edit_form': edit_form, 'category_id': product.category_id}

    return render(request, 'adminapp/product_edit.html', context=content)


def product_delete(request, pk):
    title = 'админка/продукты/удаление'

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('adminapp:products', args=[product.category_id]))

    content = {'title': title, 'product_to_delete': product}

    return render(request, 'adminapp/product_delete.html', content)

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from mainapp.models import Product, ProductCategory
from authapp.models import ShopUser
from .forms import ShopUserEditForm, ShopUserCreateForm
from .forms import ProductCategoryEditForm, ProductCategoryCreateForm
from .forms import ProductCreateForm, ProductEditForm


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return HttpResponseRedirect(reverse('adminapp:categories'))


class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    context_object_name = 'objects'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/пользователи'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'админка/пользователи'
#
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     context = {
#         'title': title,
#         'objects': users_list
#     }
#
#     return render(request, 'adminapp/users.html', context=context)

class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user_create.html'
    form_class = ShopUserCreateForm
    success_url = reverse_lazy('adminapp:users')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/пользователи/создание'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     title = 'админка/пользователи/создание'
#
#     if request.method == 'POST':
#         create_form = ShopUserCreateForm(request.POST, request.FILES)
#         if create_form.is_valid():
#             create_form.save()
#             return HttpResponseRedirect(reverse('adminapp:users'))
#     else:
#         create_form = ShopUserCreateForm()
#
#     content = {'title': title, 'create_form': create_form}
#
#     return render(request, 'adminapp/user_create.html', context=content)


class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_edit.html'
    form_class = ShopUserEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/пользователи/редактирование'
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return HttpResponseRedirect(reverse_lazy('adminapp:user_update', kwargs={'pk': user.pk}))

    # def post(self, request, *args, **kwargs):
    #     self.pk = self.kwargs['pk']
    #     return HttpResponseRedirect(reverse_lazy('adminapp:user_update', kwargs={'pk': self.pk}))

# @user_passes_test(lambda u: u.is_superuser)
# def user_update(request, pk):
#     title = 'админка/пользователи/редактирование'
#
#     user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = ShopUserEditForm(request.POST, request.FILES, instance=user)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('adminapp:user_update', args=[user.pk]))
#     else:
#         edit_form = ShopUserEditForm(instance=user)
#
#     content = {'title': title, 'edit_form': edit_form}
#
#     return render(request, 'adminapp/user_edit.html', context=content)


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    context_object_name = 'user_to_delete'
    success_url = reverse_lazy('adminapp:users')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/пользователи/удаление'
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     title = 'админка/пользователи/удаление'
#
#     user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         user.delete()
#         return HttpResponseRedirect(reverse('adminapp:users'))
#
#     content = {'title': title, 'user_to_delete': user}
#
#     return render(request, 'adminapp/user_delete.html', content)


class CategoriesListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'
    context_object_name = 'objects'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/категории'
        return context

# def categories(request):
#     title = 'админка/категории'
#
#     categories_list = ProductCategory.objects.all()
#
#     context = {
#         'title': title,
#         'objects': categories_list
#     }
#
#     return render(request, 'adminapp/categories.html', context)


class CategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_create.html'
    form_class = ProductCategoryCreateForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/категории/создание'
        return context

# def category_create(request):
#     title = 'админка/категории/создание'
#
#     if request.method == 'POST':
#         create_form = ProductCategoryCreateForm(request.POST, request.FILES)
#         if create_form.is_valid():
#             create_form.save()
#             return HttpResponseRedirect(reverse('adminapp:categories'))
#     else:
#         create_form = ProductCategoryCreateForm()
#
#     content = {'title': title, 'create_form': create_form}
#
#     return render(request, 'adminapp/category_create.html', context=content)


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_edit.html'
    form_class = ProductCategoryEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/категории/редактирование'
        return context

    def form_valid(self, form):
        category = form.save(commit=False)
        category.save()
        return HttpResponseRedirect(reverse_lazy('adminapp:category_update', kwargs={'pk': category.pk}))

# def category_update(request, pk):
#     title = 'админка/категории/редактирование'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=category)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('adminapp:category_update', args=[category.pk]))
#     else:
#         edit_form = ProductCategoryEditForm(instance=category)
#
#     content = {'title': title, 'edit_form': edit_form, 'category_to_update': category}
#
#     return render(request, 'adminapp/category_edit.html', context=content)


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    context_object_name = 'category_to_delete'
    success_url = reverse_lazy('adminapp:categories')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/категории/удаление'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

# def category_delete(request, pk):
#     title = 'админка/категории/удаление'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         category.is_active = False
#         category.save()
#         return HttpResponseRedirect(reverse('adminapp:categories'))
#
#     content = {'title': title, 'category_to_delete': category}
#
#     return render(request, 'adminapp/category_delete.html', content)


class ProductsListView(ListView):
    template_name = 'adminapp/products.html'
    context_object_name = 'objects'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.cat_pk = self.kwargs['pk']
        self.queryset = Product.objects.filter(category__pk=self.cat_pk).order_by('name')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/продукт'
        context['category'] = ProductCategory.objects.get(pk=self.cat_pk)
        context['objects'] = Product.objects.filter(category__pk=self.cat_pk).order_by('name')
        return context

# def products(request, pk):
#     title = 'админка/продукт'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#     products_list = Product.objects.filter(category__pk=pk).order_by('name')
#
#     context = {
#         'title': title,
#         'category': category,
#         'objects': products_list,
#     }
#
#     return render(request, 'adminapp/products.html', context)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product_create.html'
    form_class = ProductCreateForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/продукты/создание'
        context['category_pk'] = self.cat_pk
        return context

    def get(self, request, *args, **kwargs):
        self.cat_pk = self.kwargs['pk']
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        new_product = form.save(commit=False)
        new_product.category_id = self.kwargs['pk']
        new_product.save()

        return HttpResponseRedirect(reverse_lazy('adminapp:products', kwargs={'pk': self.kwargs['pk']}))

# def product_create(request, pk):
#     title = 'админка/продукты/создание'
#
#     if request.method == 'POST':
#         create_form = ProductCreateForm(request.POST, request.FILES)
#         if create_form.is_valid():
#             new_product = create_form.save(commit=False)
#             new_product.category_id = pk
#             new_product.save()
#             return HttpResponseRedirect(reverse('adminapp:products', args=[pk]))
#     else:
#         create_form = ProductCreateForm()
#
#     content = {'title': title, 'create_form': create_form, 'category_pk': pk}
#
#     return render(request, 'adminapp/product_create.html', context=content)


def product_read(request, pk):
    pass


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/product_edit.html'
    form_class = ProductEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/продукты/редактирование'
        context['category_id'] = self.cat_pk
        return context

    def get(self, request, *args, **kwargs):
        product = Product.objects.get(pk=kwargs['pk'])
        self.cat_pk = product.category_id
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        return HttpResponseRedirect(reverse_lazy('adminapp:product_update', kwargs={'pk': product.pk}))

# def product_update(request, pk):
#     title = 'админка/продукты/редактирование'
#
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = ProductEditForm(request.POST, request.FILES, instance=product)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('adminapp:product_update', args=[product.pk]))
#     else:
#         edit_form = ProductEditForm(instance=product)
#
#     content = {'title': title, 'edit_form': edit_form, 'category_id': product.category_id}
#
#     return render(request, 'adminapp/product_edit.html', context=content)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    context_object_name = 'product_to_delete'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/продукты/удаление'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(reverse_lazy('adminapp:products', kwargs={'pk': self.object.category_id}))

# def product_delete(request, pk):
#     title = 'админка/продукты/удаление'
#
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         product.is_active = False
#         product.save()
#         return HttpResponseRedirect(reverse('adminapp:products', args=[product.category_id]))
#
#     content = {'title': title, 'product_to_delete': product}
#
#     return render(request, 'adminapp/product_delete.html', content)

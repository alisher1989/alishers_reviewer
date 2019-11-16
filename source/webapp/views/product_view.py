from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class ProductsView(ListView):
    template_name = 'product/list.html'
    model = Product
    context_key = 'products'


class ProductView(DetailView):
    template_name = 'product/product.html'
    context_object_name = 'product'
    model = Product


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'product/create.html'
    form_class = ProductForm
    permission_required = 'webapp.add_product'
    permission_denied_message = '403 Доступ запрещен'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/update.html'
    form_class = ProductForm
    context_object_name = 'product'
    permission_required = 'webapp.change_product'
    permission_denied_message = '403 Доступ запрещен'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    pk_kwargs_url = 'pk'
    template_name = 'product/delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('webapp:products_view')
    permission_required = 'webapp.delete_product'
    permission_denied_message = '403 Доступ запрещен'


    # def get_success_url(self):
    #     return reverse('webapp:product_view', kwargs={'pk': self.object.pk})



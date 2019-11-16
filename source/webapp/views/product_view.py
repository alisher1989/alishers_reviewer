from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class TypesView(ListView):
    template_name = 'product/list.html'
    model = Product
    context_key = 'products'


class ProjectView(DetailView):
    template_name = 'product/product.html'
    context_object_name = 'product'
    model = Product


class ProjectCreateView(CreateView):
    model = Product
    template_name = 'product/create.html'
    form_class = ProductForm



class ProjectUpdateView(UpdateView):
    model = Product
    template_name = 'product/update.html'
    form_class = ProductForm
    context_object_name = 'product'


class ProjectDeleteView(DeleteView):
    model = Product
    pk_kwargs_url = 'pk'
    template_name = 'product/delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('webapp:projects_view')



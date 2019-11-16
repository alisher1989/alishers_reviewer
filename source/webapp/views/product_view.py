from django.views.generic import ListView, DetailView, CreateView

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
    form_class = ProjectForm

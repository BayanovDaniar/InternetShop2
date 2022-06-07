from django.shortcuts import render
from django.views.generic import DetailView, View
from django.contrib.contenttypes.models import ContentType
from .models import Notebook, Smartphone, Category, LatestProducts
from .mixins import CategoryDetailMixin


class HomeView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_slidebar()
        products = LatestProducts.objects.get_products_for_main_page(
            'notebook', 'smartphone'
        )
        return render(request, 'page_home/index.html', {'products': products, 'categories': categories})


class BaseView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_slidebar()
        # products = LatestProducts.objects.get_products_for_main_page()
        return render(request, 'GenericTemplate/Header_temp.html', {'categories': categories})


class CategoryDetailView(CategoryDetailMixin, DetailView):

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductDetailView(CategoryDetailMixin, DetailView):
    CT_MODEL_MODEL_CLASS = {
        'notebook': Notebook,
        'smartphone': Smartphone
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, *kwargs)

    context_object_name = 'product'
    template_name = 'product.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['ct_model'] = self.model._meta.model_name
        return context

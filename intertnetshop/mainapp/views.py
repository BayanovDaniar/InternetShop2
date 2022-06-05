from django.shortcuts import render
from django.views.generic import DetailView, View
from .models import Notebook, Smartphone, Category
from .mixins import CategoryDetailMixin


class BaseView(View):
    def get(self,request, *args, **kwargs):
        categories = Category.objects.get_categories_for_slidebar()
        return render(request, 'GenericTemplate/Header_temp.html', {'categories': categories})



class CategoryDetailView(CategoryDetailMixin, DetailView):

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'


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

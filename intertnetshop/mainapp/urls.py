from django.urls import path, re_path
from .views import ProductDetailView, CategoryDetailView, BaseView


urlpatterns = [
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name = 'category_detail'),
    path('categoriestaste', BaseView.as_view() , name = 'base')
]

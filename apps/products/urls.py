from django import views
from django.urls import path, re_path

from apps.products.views import view_brand, view_color, view_modelp, view_product, view_size


urlpatterns  = [
    path('brand/', view_brand.as_view()),
    path('color/',view_color.as_view()),
    path('modelp/', view_modelp.as_view()),
    path('size/', view_size.as_view()),
    path('product/', view_product.as_view()),
]

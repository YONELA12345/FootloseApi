from django import views
from django.urls import path, re_path
from .views import get_product_image
from django.conf import settings
from django.conf.urls.static import static
from apps.products.views import view_brand, view_color, view_image, view_modelp, view_product, view_size
from . import views

urlpatterns  = [
    path('brand/', view_brand.as_view()),
    path('color/',view_color.as_view()),
    path('modelp/', view_modelp.as_view()),
    path('size/', view_size.as_view()),
    path('product/', view_product.as_view()),
    path('image/', view_image.as_view()),
    path('products/image/<int:product_id>/', view_image.as_view(), name='product_image'),
    path('products/image/<str:image_path>/', views.show_image, name='show_image'),
    path('products/image/<int:product_id>/', get_product_image, name='get_product_image'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
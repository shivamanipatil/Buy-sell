from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import (
    ProductListView, 
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView)

urlpatterns = [
    path('',ProductListView.as_view() , name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
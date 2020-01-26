from django.urls import path
from . import views
from .views import (
    ProductListView, 
    ProductDetailView,
    ProductCreateView)

urlpatterns = [
    path('',ProductListView.as_view() , name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
]
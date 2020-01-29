from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Product
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    context = {
        'products' : Product.objects.all()
    }
    return render(request, 'store/home.html', context) 

class ProductListView(ListView):
    """Class based view for displaying Product"""
    model = Product
    template_name = 'store/home.html'
    context_object_name = 'products'
    
class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(LoginRequiredMixin, CreateView):
    """Class based view for creating a new Product with login required mixin"""
    model = Product
    fields = ['name', 'description', 'age', 'cost', 'image1', 'image2']
    
    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Class based view for updating a Product with login required mixin"""
    model = Product
    fields = ['name', 'description', 'age', 'cost', 'image1', 'image2']
    
    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)
    
    # function for testing if user tying to udpate the product is seller itself
    def test_func(self):
        product = self.get_object()
        if self.request.user == product.seller:
            return True
        return False

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'   #setting success url to home
    # function for testing if user tying to delete the product is seller itself
    def test_func(self):
        product = self.get_object()
        if self.request.user == product.seller:
            return True
        return False
    
    
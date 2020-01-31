from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib import messages
from users.models import Transaction
from django.contrib.auth.models import User


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
    
    
        
@login_required
def BuyProduct(request, pk):
    """ View and logic for buying a product"""
    product = get_object_or_404(Product, pk=pk)
    user = request.user
    buyerInstance = User.objects.get(username=request.user.username)
    sellerInstance = User.objects.get(username=product.seller.username)
    
    #if seller tries to buy him own item
    if user == product.seller:
        return redirect('home')
        
    #wallet should contain more money than cost
    if user.profile.wallet >= product.cost:
        user.profile.wallet -= product.cost
        product.seller.profile.wallet += product.cost
        new_trans = Transaction.objects.create(item=product.name, buyer=buyerInstance, seller=sellerInstance, value=product.cost)
        user.save()
        product.seller.save()
        product.delete()
        messages.success(request, f'Item successfully bought!')
    else:
        messages.error(request, f'Item cannot be bought not enough money!')
    return redirect('home')
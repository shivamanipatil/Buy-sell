from django.shortcuts import render
from .models import Product
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)


def home(request):
    context = {
        'products' : Product.objects.all()
    }
    return render(request, 'store/home.html', context) 

class ProductListView(ListView):
    model = Product
    template_name = 'store/home.html'
    context_object_name = 'products'
    
class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'age', 'cost']
    
    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

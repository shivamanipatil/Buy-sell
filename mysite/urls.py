from django.contrib import admin
from django.urls import path, include
import store.views 
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('register/', user_views.register, name='register'),
]
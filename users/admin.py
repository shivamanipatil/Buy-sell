from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Transaction, Profile


admin.site.register(Transaction)
admin.site.register(Profile)

from django.contrib import admin
from .models import Category, Post, LocalUser


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(LocalUser)

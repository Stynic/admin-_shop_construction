from django.contrib import admin
from .models import Post


class AdminBlog(admin.ModelAdmin):
    list_display = ['title', 'description', 'technology', 'image']
    fields = ['title', 'description', 'technology', 'image']


admin.site.register(Post, AdminBlog)

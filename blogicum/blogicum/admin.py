from django.contrib import admin

from django_sprint3.blogicum.blog.models import Post, Category, Location

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Location)

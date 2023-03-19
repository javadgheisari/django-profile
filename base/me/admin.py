from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created', 'updated')
    search_fields = ("title__startswith", )
    list_filter = ("created", "updated")
    
admin.site.register(Blog, BlogAdmin)

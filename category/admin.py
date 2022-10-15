from django.contrib import admin
from .models import Category


# Prepopulating slug field
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')


# Register your models here. Registered models can be seen in admin page
admin.site.register(Category, CategoryAdmin)

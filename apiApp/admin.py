from django.contrib import admin
from .models import blogs,category

class blogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    

# Register your models here.
admin.site.register(blogs,blogAdmin)
admin.site.register(category)
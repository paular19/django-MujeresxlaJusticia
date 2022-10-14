from django.contrib import admin
from .models import Links

# Register your models here.
# class LinksAdmin(admin.ModelAdmin):
#     readonly_fields= ('created', 'updated')

admin.site.register(Links)
from django.contrib import admin
from .models import Monster

class ApiAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Monster, ApiAdmin)
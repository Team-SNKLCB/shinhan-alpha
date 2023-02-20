from django.contrib import admin
from .models import Apps

# Register your models here.
@admin.register(Apps)
class AppsAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin
from .models import Mission
# Register your models here.

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    pass

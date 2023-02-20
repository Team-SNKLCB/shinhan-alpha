from django.contrib import admin
from .models import User, UserApps

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(UserApps)
class UserAppsAdmin(admin.ModelAdmin):
    pass
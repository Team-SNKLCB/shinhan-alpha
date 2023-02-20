from django.contrib import admin
from .models import Reward
# Register your models here.

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    pass

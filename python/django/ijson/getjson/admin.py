from django.contrib import admin
from .models import ImpApply


@admin.register(ImpApply)
class ImpApplyAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp')

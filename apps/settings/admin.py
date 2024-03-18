from django.contrib import admin

from apps.settings.models import Setting
# Register your models here.

@admin.register(Setting)

class Settingadmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'logo')

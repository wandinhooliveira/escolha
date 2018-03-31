from django.contrib import admin
from .models import Disputa
# Register your models here.

class DisputaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(Disputa, DisputaAdmin)
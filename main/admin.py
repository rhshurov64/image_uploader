from django.contrib import admin
from .models import Uploader

# Register your models here.
@admin.register(Uploader)
class UploaderAdmin(admin.ModelAdmin):
    list_display =('tittle','desc','image')
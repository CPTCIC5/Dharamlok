from django.contrib import admin
from .models import Stock


# Register your models here.
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    class Meta:
        fields = ['__all__']

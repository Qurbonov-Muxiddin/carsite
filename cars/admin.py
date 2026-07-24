from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Brand, Car


@admin.register(Brand)
class BrandAdmin(ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


@admin.register(Car)
class CarAdmin(ModelAdmin):
    list_display = [
    "id",
    "name",
    "brand",
    "year",
    "price",
    "isActive",
    "created_at",
]
    list_filter = ["brand", "year",'isActive']
    search_fields = ["name"]
    list_editable = [
    "price",
    "isActive",
]

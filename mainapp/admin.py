from django.contrib import admin
from .models import Product, SubmittedCloth

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "created_at")
    search_fields = ("name",)
    ordering = ("-created_at",)
    fieldsets = (
        (None, {"fields": ("name", "price", "image", "story")}),
    )

@admin.register(SubmittedCloth)
class SubmittedClothAdmin(admin.ModelAdmin):
    list_display = ("brand", "size", "submitted_at")
    search_fields = ("brand", "size")
    ordering = ("-submitted_at",)
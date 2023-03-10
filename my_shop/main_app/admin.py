from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "adress",)
    search_fields = ("email", "phone","name__startswith","adress",)

@admin.register(Category)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ("category_name",)
    list_filter = ("category_name",)
    prepopulated_fields = {"category_slug":("category_name",),}

@admin.register(Products)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "category", "price", "count", "image_show", "isActive", "updated",)
    list_filter = ("category","isActive","updated",)
    search_fields = ("code", "title","updated",)
    prepopulated_fields = {"product_slug":("title","code",),}

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='30' />".format(obj.image.url))
        return "None"
    
    image_show.__name__ = "фото"

@admin.register(Orders)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ("order_number", "order_time","ordered_by",)
    list_filter = ("order_number", "order_time",)
    search_fields = ("order_number",)

    
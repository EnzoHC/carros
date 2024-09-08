from django.contrib import admin
from cars.models import Car, Brand


class CarAdmin(admin.ModelAdmin):
    # lista de campos que aparecem na interface
    list_display = ("model", "brand", "factory_year", "model_year", "value")
    # Campos que a busca percorre
    search_fields = ("model", "brand__name")


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)

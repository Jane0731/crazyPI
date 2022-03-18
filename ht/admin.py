from django.contrib import admin
from .models import temperature_humidity


class HTAdmin(admin.ModelAdmin):
    list_display = [field.name for field in temperature_humidity._meta.fields]
    search_fields = [field.name for field in temperature_humidity._meta.fields]


admin.site.register(temperature_humidity, HTAdmin)


from django.contrib import admin
from .models import Brand, Types, Car, CarInstance

admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(Types)
admin.site.register(CarInstance)
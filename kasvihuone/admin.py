from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Greenhouse)
admin.site.register(Soilmoisture)
admin.site.register(Humidity)
admin.site.register(Temperature)
admin.site.register(Planter)


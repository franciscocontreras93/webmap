from django.contrib.gis import admin
from .models import WorldBorder, TiendasChedraui

admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(TiendasChedraui, admin.OSMGeoAdmin)


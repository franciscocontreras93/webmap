from django.contrib.gis.db import models

# Create your models here.

class WorldBorder(models.Model):

 # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2, null=True)
    iso3 = models.CharField('3 Digit ISO', max_length=3,null=True)
    un = models.IntegerField('United Nations Code', null=True)
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code', null=True)
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.

    def __str__(self):
        pass


class TiendasChedraui(models.Model):
    id_mg = models.BigIntegerField()
    nombre = models.CharField(max_length=254, null=True)
    formato = models.CharField(max_length=254,null=True)
    latitud = models.FloatField(null=True)
    longitud = models.FloatField(null=True)
    geom = models.MultiPointField(srid=4326)






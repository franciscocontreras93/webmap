from django.shortcuts import render
from .models import WorldBorder, TiendasChedraui
from django.core.serializers import serialize
import json
import ast

# Create your views here.


def index(request):

    
    

    cLayer = WorldBorder.objects.get(name='Mexico')
    pais = cLayer.mpoly.geojson

    tiendas = serialize('geojson',TiendasChedraui.objects.all(),geometry_field='geom',fields=('id_mg','nombre','longitud','latitud','formato'))
    tdaChedraui = serialize('geojson', TiendasChedraui.objects.filter(
        formato="CHEDRAUI"), geometry_field='geom', fields=('id_mg', 'formato', 'nombre', 'longitud', 'latitud'))

    tLayer = TiendasChedraui.objects.get(id_mg=1050)
    tienda = tLayer.geom.geojson

    return render(request,'webmap/index.html', { 
        'title':'Webmap BRT',
        'pais': pais,
        'tienda':tienda,
        'tiendas':tiendas,
        'tdaChedraui': tdaChedraui 


    })

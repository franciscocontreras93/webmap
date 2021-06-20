from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder, TiendasChedraui


# Auto-generated `LayerMapping` dictionary for WorldBorder model
tiendaschedraui_mapping = {
    'id_mg': 'ID MG',
    'nombre': 'NOMBRE CHE',
    'formato': 'FORMATO',
    'latitud': 'LATITUD',
    'longitud': 'LONGITUD',
    'geom': 'MULTIPOINT',
}

chedraui_shape = Path(__file__).resolve().parent / 'data' / 'CHEDRAUI_TDAS_2021.shp'

def run(verbose = True):
    lm = LayerMapping(TiendasChedraui, str(chedraui_shape),
                      tiendaschedraui_mapping, transform=False)
    lm.save(strict=False, verbose=verbose)






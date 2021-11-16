import json
from Wells.models import Well
'''
This is a roadmap to create new Wells.
Loop into a json
'''
# - Loads a JSON
with open('/Users/giba/Pedro_Work/MONUMENTO/_MASTER_APPS/Pocos_API/AGP_MASTER.json') as j:
    data=json.load(j)

# - Loop the dict and creates models
for x in data:
    # - FLoats the XY for UTC data.
    lat =float( x['LATITUDE'][0:9])
    long = float( x['LONGITUDE'][0:9])
    w = Well(id = x['POCO'], bacia=x['BACIA'],estado=x['ESTADO'], municipio=x['MUNICIPIO'], lat=lat, long=long, formac=x['FORMAC'])

     # - MAKE SURE TO SAVE
    w.save()
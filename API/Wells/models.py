from django.db import models
from django.conf import settings



class Well(models.Model):
    '''
    Well Representation class.
    You can customize the well class as you want.
    Add fields or translate them from Portuguese.
    bacia = Sedimentary Basin

    Make sure to add them to the serializer too.

    Classe para representar Poços.

    '''
    # - ID is the name of the WEll
    id = models.CharField(max_length=30,blank=False,primary_key=True)
    # - STATE, CITY, SEDIMENTARY BASIN 
    bacia = models.CharField(max_length=30,blank=False)
    # - State
    estado = models.CharField(max_length=30,blank=False)
    municipio = models.CharField(max_length=30,blank=False)
    # - GIS DATA
    lat = models.FloatField(blank=False)
    long = models.FloatField(blank=False)

    # - Campo para o dicionário de formações que o Poço Contem
    formac = models.TextField()

    # ADD MORE DATA HERE:



class User_Well(models.Model):
    '''
    Well Representation class.
    You can customize the well class as you want.
    Add fields or translate them from Portuguese.
    bacia = Sedimentary Basin

    Make sure to add them to the serializer too.

    Classe para representar Poços.

    '''
    # - ID is the name of the WEll
    id = models.CharField(max_length=30,blank=False,primary_key=True)
    # - Owner
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='snippets', on_delete=models.CASCADE)
    # - STATE, CITY, SEDIMENTARY BASIN 
    bacia = models.CharField(max_length=30,blank=False)
    # - State
    estado = models.CharField(max_length=30,blank=False)
    municipio = models.CharField(max_length=30,blank=False)
    # - GIS DATA
    lat = models.FloatField(blank=False)
    long = models.FloatField(blank=False)

    # - Campo para o dicionário de formações que o Poço Contem
    formac = models.TextField()

    # ADD MORE DATA HERE:
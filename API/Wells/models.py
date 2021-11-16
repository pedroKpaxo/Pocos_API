from django.db import models



class Well(models.Model):
    '''
    Classe para representar Poços.
    '''

    id = models.CharField(max_length=30,blank=False,primary_key=True)
    
    bacia = models.CharField(max_length=30,blank=False)
    estado = models.CharField(max_length=30,blank=False)
    municipio = models.CharField(max_length=30,blank=False)
    lat = models.FloatField(blank=False)
    long = models.FloatField(blank=False)
    # - Campo para o dicionário de formações que o Poço Contem
    formac = models.TextField()



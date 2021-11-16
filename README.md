# POCOS API

Uma API para informações geográficas de poços de petroleo.
An API for well geographic information.

Build with Django-Rest Framework.
With support for GIS models, with the DFR-GIS framework.

[preview](intropic.png)

There are two main features.
One is a public list, that no one but the admin can Update and Delete.
```sh
curl http://127.0.0.1:8000/pocos/
```
The other well list is a list created by the users
```sh
curl http://127.0.0.1:8000/users_pocos/
```


It can query for sedimentary basins and state.
Can receive custom **page_size** and **page_number** .

```sh
curl http://127.0.0.1:8000/pocos/?page_size=100
```


**Perfoming a filtered query**:

```sh
curl http://127.0.0.1:8000/pocos/?bacia=PARNAIBA&estado=MA&municipio=
```

Auth Endpoints with all-auth.
Profile picture field in custom User.

Custom Permission for OwnerOrReadOnly.
more on [Auth](#Auth)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Querys](#querys)
- [Auth](#Auth)


## Installation

Clone this repository, or download the project.
Then, in terminal, make sure to start a virtual enviroment with:

```sh
python -m venv venv
```
After that,activate the venv and install the required packages with:

```sh
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
Load some well data, and quick deliver it.
- [The well model](#The_Well_Model)
- [The well Serializer](#The_Well_Serializer)
- [Loading data](#Loadin_Data)
- [The Well views](#The_Well_Views)
- [Wells Urls](#WellsUrls)

#### The_Well_Model
The well model was built to receive the name of the well as the id,
 so we can have a Detail View for a single well queryset, the sedimentary basin (bacia),
 the state(estado), city (municipio), latitude and longitude float for UTC coordinates.


```py
class Well(models.Model):
    '''
    Well Representation class.
    bacia = Sedimentar yBasin
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

```

You can customize the well class as you want.
So, if you have data about the elevation, one could add:
```py
class Well(models.Model):
    '''
    Well Representation class.
    bacia = Sedimentar yBasin
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
    # - Elevation data:
    elevation = models.FloatField(blank=False)

```
#### The_Well_Serializer:

Simple Serializer, extending the ModelSerializer,
If you add more fields in the model, add them here in the fields area

```py
class WellSerializer(serializers.ModelSerializer):
    '''
    Basic serializer class for the Well Model, extending the ModelSerializer class.
    '''
    class Meta:
        model = Well
        fields = ['id', 'bacia', 'estado', 'municipio', 'lat', 'long','formac']

```

#### Loadin_Data
One way to load data to our API is to acess the shell, and loop to a JSON object.
I included a file called LoadWell in the Helpers Module, that can handle that.
You can customize it the way you want.
I also included well information about 597 well logs in Northeast Brazil. :) 
So, make sure to modify the path to the json object


```py
import json
from Wells.models import Well
# - Modify the path and the DIC as needed.
with open('AGP_MASTER.json') as j:
    data=json.load(j)
for x in data:
     lat =float( x['LATITUDE'][0:9])
     long = float( x['LONGITUDE'][0:9])
     w = Well(id = x['POCO'], bacia=x['BACIA'],estado=x['ESTADO'], municipio=x['MUNICIPIO'], lat=lat, long=long, formac=x['FORMAC'])
     w.save()
```
The example above can be replicated with different methods, but I personaly like these one.

#### The_Well_Views
 
There are two main views in the Well.views.
One for the complete queryset, anf filtering.
And other for the the individual well. 
```py

class WellList(generics.ListAPIView):
    """
    Retrieve,  all the well instances.
    """
    
    queryset= Well.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # - Serializer
    serializer_class = WellSerializer

    # - The filters 
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # - Custom Pagination,
    pagination_class = CustomPageNumberPagination
    filterset_fields = ['bacia', 'estado','municipio']
    

class WellDetail(APIView):
    """
    Retrieve,  well instance.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Well.objects.get(pk=pk)
        except Well.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        '''
        Gets a single Well fronm the main list
        '''
        well = self.get_object(pk)
        serializer = WellSerializer(well)
        return Response(serializer.data)

class User_WellList(generics.ListAPIView):
    """
    Retrieve,  all the well instances created by our users.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset= User_Well.objects.all()

    # - Serializer
    serializer_class = UserWellSerializer

    # - The filters 
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # - Custom Pagination,
    pagination_class = CustomPageNumberPagination
    filterset_fields = ['bacia', 'estado','municipio','owner']

class Create_User_Well(generics.CreateAPIView):
    """
    Retrieve,  well instance.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserWellSerializer

class Update_User_well(generics.RetrieveUpdateDestroyAPIView):
    '''
    CRUD VIEW for updating and deleting
    '''
    serializer_class= UserWellSerializer
    permission_class = IsOwnerOrReadOnly
```
### WellsUrls
The Url system for the well lists.

```py
urlpatterns = [
    # - Main query Url
    path('pocos/', views.WellList.as_view()),
    # - Individual Query
    path('pocos/<str:pk>/', views.WellDetail.as_view()),
    # - Well Created by the users
    path('users_pocos/', views.User_WellList.as_view()),
    # - View for creating a well
    path('create_poco/',views.Create_User_Well.as_view()),
    # - View for owner to CRUD
    path('users_pocos/<str:pk>/', views.Update_User_well.as_view()),
```
## Query

The views in Wells.models.py are equipped with django-filters.
One could query for States, City, and Sedimentary Basin.

This is a sample url with Search Fields.:

**http://127.0.0.1:8000/pocos/?bacia=PARNAIBA&estado=MA&municipio=**

## Auth


Auth is done with the help of [Django-All-Auth](https://django-allauth.readthedocs.io/en/latest/index.html) , 
and [Django-Rest-Auth](https://django-rest-auth.readthedocs.io/en/latest/index.html). 

If you want to customize it, make sure to check the 'settings.py' file in the main API folder.
**REMEMBER** to use the settings.AUTH_USER_MODEL, in Users created models.

Custom permission in Helpers Module.

```py
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
```
#### Custom Ownership
In the User_well Model the is a custom ownership implemented, overriding the default auth.User.

```py
owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='snippets', on_delete=models.CASCADE)
```
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Wells import views

urlpatterns = [
    path('pocos/', views.WellList.as_view()),
    path('pocos/<str:pk>/', views.WellDetail.as_view()),
]
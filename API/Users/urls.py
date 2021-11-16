from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Users import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('register/', views.UserCreation.as_view()),
    
]
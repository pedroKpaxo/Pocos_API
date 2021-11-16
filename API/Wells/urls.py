from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Wells import views

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
]
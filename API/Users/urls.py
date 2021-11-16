from django.urls import path, include
from Users import views
from django.conf.urls import url
from allauth.account.views import confirm_email

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('register/', views.UserCreation.as_view()),

    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
    
]
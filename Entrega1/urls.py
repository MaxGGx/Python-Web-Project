from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns = [
    path("login/", segunda_vista),
    path("", inicio),
    path("logout/", logout),
    path("register/", registro)
]
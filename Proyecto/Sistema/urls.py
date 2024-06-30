from django.urls import path
from .views import *

urlpatterns = [
   path('',Home,name="home"),
   path("listar/",Listar,name="listar"),
     path('registrar/',Registrar,name="registrar"),
]

from django.urls import path,include 
from SeguridadApp.views import acceder, homePage, salir
urlpatterns = [ path('',acceder,name="login"), path('home/', homePage, name='home'),
path('logout/',salir,name='logout')] 
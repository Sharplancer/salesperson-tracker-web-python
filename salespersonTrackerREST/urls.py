
from django.contrib import admin
from django.urls import include, path
from django.conf import settings 
from django.conf.urls.static import static
from . import views 


urlpatterns = [
 
   path('home',views.home,name='home'),
   
    
]
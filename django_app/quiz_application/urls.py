from django.urls import path
from . import views  #importing our view file 

urlpatterns = [
    path("", views.homepage, name="home"),
    path("viewcard", views.addcard, name="viewcard"),
    path("addcard", views.addcard, name="addcard"), #mapping the homepage function
]
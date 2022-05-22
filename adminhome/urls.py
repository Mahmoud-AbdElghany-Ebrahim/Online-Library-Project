from django.urls import path 
from . import views
urlpatterns=[
    path('', views.Ahome , name = 'AdminH'),

]
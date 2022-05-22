from django.urls import path
from . import views

urlpatterns=[
    path('logIn', views.logIn, name="logIn"),
    path('signUp', views.signUp, name="signUp"),
    path('update/<int:id>',views.update, name="update"),
]
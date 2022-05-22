from django.urls import path
from . import views

urlpatterns = [
    path('allBooks', views.index, name='index'),
    path('studentBooks', views.Student, name='studentBooks'),
    path('borrowBook/<int:id>', views.borrowed, name='borrowBook'),
    path('returnBook/<int:id>', views.returned, name='returnBook'),
    path('addBook', views.add, name='add'),
    path('update/<int:id>' , views.update, name='update'),
    path('delete/<int:id>' , views.delete, name='delete'),
    path('extend/<int:id>' , views.extend, name='extend'),

]
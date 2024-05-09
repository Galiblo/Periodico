from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarNoticia/', views.registrarNoticia),
    path('eliminacionNoticia/<id>', views.eliminacionNoticia),
    path('edicionNoticia/<id>', views.edicionNoticia),
    path('editarNoticia/', views.editarNoticia),
]
from django.shortcuts import render, redirect
from .models import Noticia

# Create your views here.
def home(request):
    noticias = Noticia.objects.all()
    return render(request,"home.html", {"noticias":noticias})

def registrarNoticia(request):
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']

    noticia = Noticia.objects.create(nombre=nombre, descripcion=descripcion)
    return redirect('/')

def eliminacionNoticia(request, id):
    noticia = Noticia.objects.get(id=id)
    noticia.delete()

    return redirect('/')
def edicionNoticia(request, id):
    noticia = Noticia.objects.get(id=id)
    return render(request, "edicionNoticia.html", {"noticia":noticia})

def editarNoticia(request):
    id = request.POST['noticiaID']
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']

    noticia = Noticia.objects.get(id=id)
    noticia.id = id
    noticia.nombre = nombre
    noticia.descripcion = descripcion
    noticia.save()
    return redirect('/')
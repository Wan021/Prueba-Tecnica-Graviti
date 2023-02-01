from django.shortcuts import render, redirect
from .models import Persona
from django.contrib import messages

# Create your views here.

def home(request):
    personasListadas = Persona.objects.all()
    return render(request, "GestionPersonas.html", {"personas": personasListadas})

def registrarPersona(request):
    nombre=request.POST['txtNombre']
    apellido_paterno=request.POST['txtApellidoPaterno']
    apellido_materno=request.POST['txtApellidoMaterno']
    nacionalidad=request.POST['txtNacionalidad']
    edad=request.POST['txtEdad']

    e=str(edad)
    codigo=nombre[0:2].upper()+apellido_paterno[0]+apellido_materno[0]+nacionalidad[0]+e[0]

    Persona.objects.create(codigo=codigo,nombre=nombre.capitalize(), apellido_paterno=apellido_paterno.capitalize(), apellido_materno=apellido_materno.capitalize(), nacionalidad=nacionalidad.capitalize(), edad=edad)

    messages.success(request, "¡Registro exitoso!")
    return redirect('/')    

def edicionPersona(request,codigo):
    persona=Persona.objects.get(codigo=codigo)
    return render(request, "edicionPersona.html", {"persona":persona})

def editarPersona(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido_paterno=request.POST['txtApellidoPaterno']
    apellido_materno=request.POST['txtApellidoMaterno']
    nacionalidad=request.POST['txtNacionalidad']
    edad=request.POST['txtEdad']

    persona=Persona.objects.get(codigo=codigo)
    persona.nombre = nombre
    persona.apellido_paterno = apellido_paterno
    persona.apellido_materno = apellido_materno
    persona.nacionalidad = nacionalidad
    persona.edad = edad
    persona.save()

    messages.success(request, "¡Edición exitosa!")
    return redirect('/')

def eliminacionPersona(request, codigo):
    persona=Persona.objects.get(codigo=codigo)
    persona.delete()

    messages.success(request, "¡Eliminación exitosa!")
    return redirect('/')

def cancelar(request):
    return redirect('/')

def OrderNombre(request):
    personasListadas = Persona.objects.all().order_by('nombre').values()
    return render(request, "GestionPersonas.html", {"personas": personasListadas})

def OrderAPaterno(request):
    personasListadas = Persona.objects.all().order_by('apellido_paterno').values()
    return render(request, "GestionPersonas.html", {"personas": personasListadas})

def OrderAMaterno(request):
    personasListadas = Persona.objects.all().order_by('apellido_materno').values()
    return render(request, "GestionPersonas.html", {"personas": personasListadas})

def OrderNacionalidad(request):
    personasListadas = Persona.objects.all().order_by('nacionalidad').values()
    return render(request, "GestionPersonas.html", {"personas": personasListadas})

def OrderEdad(request):
    personasListadas = Persona.objects.all().order_by('edad').values()
    return render(request, "GestionPersonas.html", {"personas": personasListadas})


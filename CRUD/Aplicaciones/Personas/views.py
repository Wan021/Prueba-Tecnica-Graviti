from django.shortcuts import render, redirect
from .models import Persona, Nacionalidades
from django.contrib import messages

# Create your views here.

def home(request):
    personasListadas = Persona.objects.all()
    naciones = Nacionalidades.objects.all()
    return render(request, "GestionPersonas.html", {"personas": personasListadas,"nacionalidades":naciones})

def registrarPersona(request):
    nombre=request.POST['txtNombre']
    apellido_paterno=request.POST['txtApellidoPaterno']
    apellido_materno=request.POST['txtApellidoMaterno']
    nacionalidad=request.POST['txtNacionalidad']
    edad=request.POST['txtEdad']
    sexo=request.POST['txtSexo']

    naciones = Nacionalidades.objects.all()
    na=''
    for n in naciones:
        if str(n.codigo)==nacionalidad:
            if sexo=='M':
                na=n.nacionalidad_masculino
            else:
                na=n.nacionalidad_femenino
    e=str(edad)
    codigo=nombre[0:2].upper()+apellido_paterno[0]+apellido_materno[0]+nacionalidad[0]+e[0]

    Persona.objects.create(codigo=codigo,nombre=nombre.capitalize(), apellido_paterno=apellido_paterno.capitalize(), apellido_materno=apellido_materno.capitalize(), nacionalidad=na.capitalize(), edad=edad, sexo=sexo)

    messages.success(request, "¡Registro exitoso!")
    return redirect('/')    

def edicionPersona(request,codigo):
    persona=Persona.objects.get(codigo=codigo)
    per=Persona.objects.filter(codigo=codigo)
    naciones = Nacionalidades.objects.all()
    na={}
    for nacion in naciones:
        if(per[0].nacionalidad.lower() == nacion.nacionalidad_masculino.lower() or per[0].nacionalidad.lower() == nacion.nacionalidad_femenino.lower()):
            na['codigo']=nacion.codigo
            na['pais']=nacion.pais
            if(per[0].sexo=='M'):
                na['sexo']='Masculino'
                na['letra']='M'
            else:
                na['sexo']='Femenino'
                na['letra']='F'
    return render(request, "edicionPersona.html", {"persona":persona,"na":na,"nacionalidades":naciones})

def editarPersona(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido_paterno=request.POST['txtApellidoPaterno']
    apellido_materno=request.POST['txtApellidoMaterno']
    nacionalidad=request.POST['txtNacionalidad']
    edad=request.POST['txtEdad']
    sexo=request.POST['txtSexo']

    naciones = Nacionalidades.objects.all()
    na=''
    for n in naciones:
        if str(n.codigo)==nacionalidad:
            if sexo=='M':
                na=n.nacionalidad_masculino
            else:
                na=n.nacionalidad_femenino
    e=str(edad)

    persona=Persona.objects.get(codigo=codigo)
    persona.nombre = nombre.capitalize()
    persona.apellido_paterno = apellido_paterno.capitalize()
    persona.apellido_materno = apellido_materno.capitalize()
    persona.nacionalidad = na.capitalize()
    persona.edad = edad
    persona.sexo = sexo
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
    naciones = Nacionalidades.objects.all()
    return render(request, "GestionPersonas.html", {"personas": personasListadas,"nacionalidades":naciones})

def OrderAPaterno(request):
    personasListadas = Persona.objects.all().order_by('apellido_paterno').values()
    naciones = Nacionalidades.objects.all()
    return render(request, "GestionPersonas.html", {"personas": personasListadas,"nacionalidades":naciones})

def OrderAMaterno(request):
    personasListadas = Persona.objects.all().order_by('apellido_materno').values()
    naciones = Nacionalidades.objects.all()
    return render(request, "GestionPersonas.html", {"personas": personasListadas,"nacionalidades":naciones})

def OrderNacionalidad(request):
    personasListadas = Persona.objects.all().order_by('nacionalidad').values()
    naciones = Nacionalidades.objects.all()
    return render(request, "GestionPersonas.html", {"personas": personasListadas,"nacionalidades":naciones})

def OrderEdad(request):
    personasListadas = Persona.objects.all().order_by('edad').values()
    naciones = Nacionalidades.objects.all()
    return render(request, "GestionPersonas.html", {"personas": personasListadas,"nacionalidades":naciones})


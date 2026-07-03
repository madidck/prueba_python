from django.shortcuts import render
from .models import Alumnos, ComentarioContacto 
from .forms import ComentarioContactoForm

# Create your views here.
def registros (request):
    alumnos=Alumnos.objects.all()
    return render(request,"registros/principal.html",{'alumnos':alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): 
            form.save()
            comentarios = ComentarioContacto.objects.all()
            return render(request, "registros/consultaContacto.html", {'comentarios': comentarios})
    form = ComentarioContactoForm()
    #si saale mal se va a reenviar al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form':form})   

def contacto(request):
    return render(request,"registros/contacto.html")

def consultarComentario(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/consultaContacto.html", {'comentarios': comentarios})
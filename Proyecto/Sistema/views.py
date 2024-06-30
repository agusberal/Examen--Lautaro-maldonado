from django.shortcuts import render, redirect
from .formularios import *
from .models import *
# Create your views here.
def Home(request):
    return render(request,"index.html")

def Registrar(request):
    data={
        'form':Nuevo_Producto()
    }
    if request.method=='POST':
        guardar=Nuevo_Producto(request.POST, request.FILES)
        if guardar.is_valid():
            guardar.save()
            data["mensaje"]="Datos Gaurdados"
        else:
            data["form"]=guardar
    return render(request,"Pages/registrar.html",data)



def Listar(request):
    Lis=Productos.objects.all()
    data={
        'lis':Lis
    }
    return render(request,"Pages/listar.html",data)
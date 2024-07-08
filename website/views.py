from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from .forms import Contactos, fomulario_usuario,Formulario_compras
from .models import Servicios,Contenido,Categoria, Productos
from django.views.generic import View
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,authenticate


# Create your views here.

def inicio(request):

    return render(request,"home.html")


def contenido(request):
    contenido = Contenido.objects.all()
    return render(request,"contenido.html",{"los_contenidos":contenido})

def servicios(request):

    servis = Servicios.objects.all()
    return render(request, "servicios.html",{"servi":servis})

def category(request,categoria_id):

    vari_categoria = Categoria.objects.get(id=categoria_id)
    vari_contenido = Contenido.objects.filter(categorias=vari_categoria)

    return render(request,"categoria.html", {"dict_categor":vari_categoria,"los_contenidos":vari_contenido})

def contactos(request):
    formu_contacto = Contactos()

    if request.method == "POST":
        formu_contacto = Contactos(data=request.POST)
        if formu_contacto.is_valid():
            asunto = request.POST.get("asunto")
            email = request.POST.get("email")
            contenido = request.POST.get("mensaje")

            vari_email = EmailMessage("Mesaje de la aplicación de pruba de django",
            "el usuario de nombre {} cuyo correo {} envía lo siguiente: \n\n {}".format(asunto,email,contenido),
            "",["micromagma47@gmail.com"],reply_to=[email])

            try:
                vari_email.send()
                return redirect("/contacta?enviado")
            except:

                redirect("/contacta?noenviado")

    return render(request,"contactos.html",{"contacto":formu_contacto})

def Tienda(request):
    merca = Productos.objects.all()

    return render(request,"tienda.html", {"articulos":merca})

class Registro(View):

    def get(self, request):
        form = fomulario_usuario()
        return render(request,"registro.html", {"formulario":form})

    def post(self, request):
        form = fomulario_usuario(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request,usuario)
            return redirect("/?registrado")
        else:
            for aviso in form.error_messages:
                messages.error(request, form.error_messages[aviso])

            return render(request, "registro.html", {"formulario": form})


def cierre_de_secion(request):
    logout(request)

    return redirect("/")

def inicio_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data.get("username")
            contrasenha = form.cleaned_data.get("password")
            autenticacion = authenticate(username = nombre_de_usuario, password = contrasenha)
            if autenticacion is not None:
                login(request,autenticacion)
                return redirect("/")
            else:
                messages.error(request,"usuario inválido")
        else:
            messages.error(request, "¡usuario o contraseña inválida!")
    form = AuthenticationForm()
    return render(request,"log.html", {"formulario_login":form})

def consultas(request):
    formulario_de_tienda = Formulario_compras()

    if request.method == "POST":
        formulario_de_tienda = Formulario_compras(data=request.POST)
        if formulario_de_tienda.is_valid():
            nombre_usuario = request.POST.get("nombre_usuario")
            nombre_articulo = request.POST.get("nombre_articulo")
            email = request.POST.get("email")
            tlf = request.POST.get("tlf")
            mensaje = request.POST.get("mensaje")

            vari_email = EmailMessage("Mensaje de la aplicación de prueba de django",
            "el usuario de nombre: {} cuyo correo: {} y tlf: {} envía lo siguiente: \n\n {} "
            " sobre el artículo: {} ".format(nombre_usuario,email,tlf,mensaje,nombre_articulo),
            "",["micromagma47@gmail.com"],reply_to=[email])

            try:
                vari_email.send()
                return redirect("/preguntas?mensaje_enviado")
            except:

                redirect("/contacta?noenviado")

    return render(request,"consultas.html",{"formulario_tienda":formulario_de_tienda})
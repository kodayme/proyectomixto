from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Contactos(forms.Form):
    asunto = forms.CharField(label="nombre",required=True, max_length=50)
    email = forms.EmailField(label="correo", required=True)
    mensaje = forms.CharField(label="preguntas",widget=forms.Textarea)

class fomulario_usuario(UserCreationForm):
    email = forms.EmailField(label='correo',required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')

class Formulario_compras(forms.Form):
    nombre_usuario = forms.CharField(label="nombre usuario", required=True, max_length=50)
    nombre_articulo = forms.CharField(label="nombre del artículo a consultar",required=True, max_length=50)
    email = forms.EmailField(label="correo", required=True)
    tlf = forms.CharField(label="tlf o whatsapp",required=True)
    mensaje = forms.CharField(label="preguntas y consultas",widget=forms.Textarea)
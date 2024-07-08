from django.urls import path
from .views import inicio,contactos,contenido,servicios,Tienda,Registro,cierre_de_secion,inicio_sesion,consultas
from . import views
urlpatterns = [
    path('', inicio, name='pagina_inicial'),
    path('contacta', contactos, name='pagina_contacto'),
    path('contenidos', contenido, name='los_contenidos'),
    path('services', servicios, name='los_servicios'),
    path('categ/<int:categoria_id>/', views.category, name='las_categorias'),
    path('tienda', Tienda, name='store'),
    path('autentic', Registro.as_view(), name='registro'),
    path('cierre', cierre_de_secion, name='cierre_session'),
    path('login', inicio_sesion, name="inicio_session"),
    path('preguntas', consultas, name="consulta_tienda"),
]
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("saludar/", views.saludo),
    path("saludar2/", views.saludo_con_input),
    path("otra-vista/", views.segunda_vista),
    path("nombre/<nombre>/<apellido>/", views.nombre),
    path("miTemplate/", views.probando_template),
    path("dia/", views.fecha_hora),
    path("azar/", views.numero_aleatorio),
]

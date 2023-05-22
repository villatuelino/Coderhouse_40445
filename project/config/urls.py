from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("_core_.urls"), name="index"),
    path("cliente/", include("cliente.urls")),
    path("venta/", include("venta.urls")),
]

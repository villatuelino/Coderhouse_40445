from django.urls import path

from .views import index

# Es necesario este nombre, para ser llamado desde la plantila,
# por ejemplo: {% url 'cliente:index' %}
app_name = "venta"

urlpatterns = [
    path("", index, name="index"),
]

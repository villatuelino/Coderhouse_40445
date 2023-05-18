from django.urls import path

from .views import crear_cliente, crear_clientes_predeterminados, index, prueba_búsqueda

# Es necesario este nombre, para ser llamado desde la plantila,
# por ejemplo: {% url 'cliente:index' %}
app_name = "cliente"

urlpatterns = [
    path("", index, name="index"),
    path("crear-clientes-predeterminados/", crear_clientes_predeterminados, name="crear-clientes"),
    path("prueba-búsqueda/", prueba_búsqueda, name="prueba-búsqueda"),
    path("crear/", crear_cliente, name="crear"),
]

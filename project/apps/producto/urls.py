from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

# *********** URLS basadas en funciones
urlpatterns = [
    # path("", views.index, name="index"),
    # path("productocategoria/list/", views.producto_categoria_list, name="productocategoria_list"),
    #     path("productocategoria/create/", views.producto_categoria_create, name="productocategoria_create"),
    #     path("productocategoria/delete/<int:pk>", views.producto_categoria_delete, name="productocategoria_delete"),
    #     path("productocategoria/update/<int:pk>", views.producto_categoria_update, name="productocategoria_update"),
    #     path("productocategoria/detail/<int:pk>", views.producto_categoria_detail, name="productocategoria_detail"),
]

# *********** URLS basadas en clases
urlpatterns += [
    path("", TemplateView.as_view(template_name="producto/index.html"), name="index"),
    path("productocategoria/list/", views.ProductoCategoriaList.as_view(), name="productocategoria_list"),
    path("productocategoria/create/", staff_member_required(views.ProductoCategoriaCreate.as_view()), name="productocategoria_create"),
    path("productocategoria/delete/<int:pk>", staff_member_required(views.ProductoCategoriaDelete.as_view()), name="productocategoria_delete"),
    path("productocategoria/update/<int:pk>", staff_member_required(views.ProductoCategoriaUpdate.as_view()), name="productocategoria_update"),
    path("productocategoria/detail/<int:pk>", views.ProductoCategoriaDetail.as_view(), name="productocategoria_detail"),
]

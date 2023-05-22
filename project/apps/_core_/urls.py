from django.urls import path

from project.config.settings import STATIC_URL

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
]
urlpatterns += STATIC_URL

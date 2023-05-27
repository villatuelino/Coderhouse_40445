from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")


# * Login basado en funciones
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def login_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "home/index.html", {"mensaje": f"Bienvenido {usuario}"})
    else:
        form = AuthenticationForm()
    return render(request, "home/login.html", {"form": form})


# * Registro basado en funciones
from . import forms


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "home/index.html", {"mensaje": "Usuario creado 👌"})
    else:
        # form = UserCreationForm()
        form = forms.UserRegisterForm()
    return render(request, "home/registro.html", {"form": form})

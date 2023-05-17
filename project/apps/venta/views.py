from django.shortcuts import render


def index(request):
    contexto = {}
    return render(request, "venta/index.html", contexto)

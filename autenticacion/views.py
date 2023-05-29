from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

class VRegistro(View):

    # Nos muestra el formulario
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registro.html", {"form":form})

    # Almacena el formulario con la info que el usuario ha introducido
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save() # Almacena la info en la bbdd
            login(request, usuario)
            return redirect("Home")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request, "registro/registro.html", {"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect("Home")

def loguear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contrasenna = form.cleaned_data.get("password")
            usuario = authenticate(username = nombre_usuario, password = contrasenna)
            if usuario is not None:
                login(request, usuario)
                return redirect("Home")
            else:
                messages.error(request, "Usuario no válido")
                return render(request, "login/login.html", {"form":form})
        else:
            messages.error(request, "Información incorrecta")
            return render(request, "login/login.html", {"form":form})
    else:
        form = AuthenticationForm()
        return render(request, "login/login.html", {"form":form})
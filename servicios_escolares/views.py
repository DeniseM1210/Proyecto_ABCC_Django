from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .models import Alumno

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

# Login
def login(request):
    return render(request, 'alumnos/login.html')

# --- CONSULTAR TODOS LOS ALUMNOS ---
class ListarAlumnos(ListView):
    model = Alumno 

#--- ALTAS ---
class CrearAlumno(SuccessMessageMixin, CreateView):
    model = Alumno
    form = Alumno
    fields = "__all__"
    success_message = "Alumno AGREGADO correctamente!!!"
    def get_success_url(self):
        return reverse('listar')


#--- BAJAS ---
class EliminarAlumno(SuccessMessageMixin, DeleteView):
    model = Alumno
    success_message = 'Alumno eliminado correctamente'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('listar')
    
# --- CAMBIOS ---
class ActualizarAlumno(SuccessMessageMixin, UpdateView):
    model = Alumno
    fields = "__all__"
    success_message = "Alumno modificado correctamente"

    def get_success_url(self):
        return reverse('listar')

#--- CONSULTAR UN ALUMNO ---
class DetalleAlumno(DetailView):
    model = Alumno



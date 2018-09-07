from django.shortcuts import render
from TODOapp.models import Task


# Create your views here.

def show_todo(request):
	diccionario = {}
	diccionario['task'] = Task.objects.all()
	return render(request, 'start.html', diccionario)

from django.shortcuts import render, redirect, HttpResponse
from TODOapp.models import Task


# Create your views here.

def show_todo(request):
	diccionario = {}
	diccionario['ts'] = Task.objects.all()
	return render(request, 'start.html', diccionario)

def gaurdar_task(request):
	if request.POST:
		content = request.POST.get('content-task')
		if content:
			nt = Task()
			nt.todo = content
			nt.archive = True
			nt.save()
		return redirect('/task')
	else:
		return HttpResponse("Es get")

def borrar(request):
	if request.POST:
		contenido = request.POST.get('contenido', None)
		if contenido:
			ide = Task.objects.get(id=contenido)
			ide.delete()
			return redirect('/task')
		else:
			return HttpResponse('No content')

def redirect_show(request):
	return redirect('/task')

def archivar(request):
	if request.POST:
		conten = request.POST.get('contenido', None)
		if conten:
			print("Hay contenido")
			ide = Task.objects.get(id=conten)
			ide.archive = False
			ide.save()
			return redirect('/task')
		else:
			return HttpResponse("No content")

def ir_a_archivados(request):
	return redirect('/archivados')

def desarchivar(request):
	if request.POST:
		contenido_a_desarchivar = request.POST.get('desarchivar', None)
		if contenido_a_desarchivar:
			aux = Task.objects.get(id=contenido_a_desarchivar)
			aux.archive = True
			aux.save()
			ir_a_archivados(request)
		return redirect('/archivados')

def show_todo_archivados(request):
	diccionario = {}
	diccionario['ts'] = Task.objects.all()
	return render(request, 'archivados.html', diccionario)

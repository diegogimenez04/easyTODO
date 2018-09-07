from django.shortcuts import render
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
            nt.save()
        return redirect("/task")
    elif request.GET:
        return HttpResponse("Es GET")
    return HttpResponse("Terminado")

"""easyTODO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from TODOapp.views import (show_todo, gaurdar_task, borrar, redirect_show, archivar, desarchivar, show_todo_archivados)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('task', show_todo, name='todo'),
    path('save', gaurdar_task, name='save'),
    path('borrar', borrar, name='borrar'),
    path('archivar', archivar, name='archivar'),
    path('archivados', show_todo_archivados, name='desarchivados'),
    path('desarchivar', desarchivar, name='desarchivar'),
    path('', redirect_show, name='redirect_show')
]

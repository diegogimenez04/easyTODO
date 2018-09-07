from django.urls import path
from TODOapp.views import show_todo

urlpatterns = [
	path('', show_todo, name="index")
]
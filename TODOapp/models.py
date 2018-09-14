from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.

class Task(models.Model):
	datetime = models.DateTimeField('Fecha', auto_now=True)
	todo = models.CharField('Que hay que hacer?', max_length=150)
	archive = models.BooleanField(default=True)


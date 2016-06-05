from django.db import models
from django.contrib import admin

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 150)
    category = models.CharField(max_length=15)
    content = models.TextField()
    timestamp = models.DateTimeField()

class Meta:
    ordering = ('-timestamp',)

admin.site.register(Blog)
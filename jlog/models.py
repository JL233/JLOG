from django.db import models
from django.contrib import admin

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 150)
    category = models.CharField(max_length=15)
    content = models.TextField()
    #auto_now_add为添加时的时间，更新对象时不会有变动。
    #auto_now无论是你添加还是修改对象，时间为你添加或者修改的时间。
    timestamp = models.DateTimeField(auto_now = True)

class Meta:
    ordering = ('-timestamp',)

admin.site.register(Blog)
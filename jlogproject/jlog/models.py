from django.db import models
from django.contrib import admin

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 150)
    category = models.CharField(max_length=15)
    content = models.TextField()
    #auto_now_add设置True表示自动设置对象增加时间
    timestamp = models.DateTimeField(auto_now_add = True)

class Meta:
    ordering = ('-timestamp',)

admin.site.register(Blog)
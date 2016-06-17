"""untitled4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from jlog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home,{'template_name': 'index.html'}),
    url(r'^create/$', views.create,{'template_name': 'write.html'}),
    url(r'^add/$', views.add,{'template_name': 'blog.html'}),
    url(r'^write/(?P<id>\d+)/$', views.write,{'template_name': 'write.html'}),
    url(r'^detail/(?P<id>\d+)/$', views.detail,{'template_name': 'blog.html'}),
    url(r'delete/(?P<id>\d+)/$',views.delete,{'template_name': 'index.html'}),
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_ROOT }),
]

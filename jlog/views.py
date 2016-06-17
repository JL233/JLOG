from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render_to_response
from jlog.models import Blog

# Create your views here.
def create(request,template_name):
    return render_to_response(template_name)
def home(request,template_name):
    blogs = Blog.objects.all()
    return render_to_response(template_name, {'blogs': blogs})
def add(request,template_name):
    if request.method == "POST":
        if "id" in request.POST:
            blog = Blog.objects.get(id=request.POST["id"])  # 查询一条你要更新的数据
        else:
            blog = Blog()

        title = request.POST["title"]
        category=request.POST.get("category",None)
        content=request.POST["content"]

        blog.title=title
        blog.category=category
        blog.content=content

        blog.save()
        # 返回注册成功页面
        return detail(request,blog.id,template_name)
    else:
        pass
def detail(request,id,template_name):
    try:
        blog = Blog.objects.get(id=str(id))
    except Blog.DoesNotExist:
        raise Http404
    return render(request, template_name, {'blog': blog})
def write(request,id,template_name):
    try:
        blog = Blog.objects.get(id=str(id))
    except Blog.DoesNotExist:
        raise Http404
    return render(request, template_name, {'blog': blog})
def delete(request,id,template_name):
    try:
        blog = Blog.objects.get(id=str(id))
        blog.delete()
    except Blog.DoesNotExist:
        raise Http404
    return render(request, template_name, {'blog': blog})
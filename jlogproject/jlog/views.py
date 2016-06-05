from django.shortcuts import render
from django.shortcuts import render_to_response
from jlog.models import Blog
# Create your views here.
def create(request):
    return render_to_response('create.html')
def home(request):
    blogs = Blog.objects.all()
    return render_to_response('index.html', {'blogs': blogs})
def add(request):
    if request.method == "POST":
        title = request.POST["title"]
        category=request.POST.get("category",None)
        content=request.POST["content"]
        blog=Blog()
        blog.title=title
        blog.category=category
        blog.content=content
        blog.save()
        # 返回注册成功页面
        return home(request)
    else:
        pass
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render_to_response
from jlog.models import Blog
# Create your views here.
def create(request):
    return render_to_response('write.html')
def home(request):
    blogs = Blog.objects.all()
    return render_to_response('index.html', {'blogs': blogs})
def add(request):
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
        return home(request)
    else:
        pass
def detail(request,id):
    try:
        blog = Blog.objects.get(id=str(id))
    except Blog.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', {'blog': blog})
def write(request,id):
    try:
        blog = Blog.objects.get(id=str(id))
    except Blog.DoesNotExist:
        raise Http404
    return render(request, 'write.html', {'blog': blog})
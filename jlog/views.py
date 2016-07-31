from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render_to_response
from jlog.models import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.
def create(request,template_name):
    return render_to_response(template_name)
def home(request,template_name):

    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)
    print(type(blogs))
    return render_to_response(template_name, {"blogs": blogs})

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

def search(request,template_name):
    print("begin search...")
    blogs=None
    if request.method == "POST":
        if "keywords" in request.POST:
            print(request.POST)
            keywords=request.POST["keywords"]
            # 模糊查询
            blogs = Blog.objects.filter(Q(title__contains=keywords) | Q(category__contains=keywords)| Q(content__contains=keywords))
    return render_to_response(template_name, {"blogs": blogs})
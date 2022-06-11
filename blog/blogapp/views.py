from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog,Category,Comment


# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request,'index.html',{'blogs':blogs})

def allCat(request,c_slug=None):
    c_page=None
    products=None
    if c_slug != None:
        c_page = get_object_or_404(Category,slug=c_slug)
        blogs=Blog.objects.all().filter(category=c_page,)
    else:
        blogs=Blog.objects.all()
    return render(request,'about.html',{'category':c_page,'blogs':blogs})
def blog(request,c_slug,b_slug):
    try:
        blogs = Blog.objects.get(category__slug=c_slug,slug=b_slug)
        comments = Comment.objects.filter(blog=blogs)
    except Exception as e:
        raise e
    if request.method == 'POST':
        name = request.POST.get('name', '')
        cmnt = request.POST.get('cmnt', '')
        task = Comment(name=name, cmnt=cmnt,blog=blogs)
        task.save()
    return render(request,'blog.html',{'blogs':blogs,'comments':comments})

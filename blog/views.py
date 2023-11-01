from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    #blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-date') # ordered by most current date
    #blogs = Blog.objects.order_by('-date')[:5] # ordered and the last 5 blog posts
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
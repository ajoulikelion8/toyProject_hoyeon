from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'crud/home.html', {'blogs':blogs})

def create(request):
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
        
    else:
        form = NewBlog()
        return render(request, 'crud/new.html', {'form':form})

def update(request, pk):
    return

def delete(request, pk):
    return
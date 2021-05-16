from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog

# Create your views here.

def homeOne(request):
    blog = Blog.objects.all()
    return render(request,'homeOne.html',{'blog' : blog})

def detailOne(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detailOne.html' ,{'blog' : blog_detail})

def newOne(request):
    return render(request,'newOne.html')

def createOne(request):
    freshBlog = Blog()
    freshBlog.blog_title = request.POST['title']
    freshBlog.blog_writer = request.POST['writer']
    freshBlog.blog_body = request.POST['body']
    freshBlog.blog_date = timezone.now()
    freshBlog.save()
    return redirect('detailOne',freshBlog.id)


def editOne(request, blog_id):
    reviseBlog = Blog.objects.get(id = blog_id)
    return render(request, 'editOne.html', {'blog' : reviseBlog})


def updateOne(request, blog_id):
    updateBlog = Blog.objects.get(id = blog_id)
    updateBlog.blog_title = request.POST['title']
    updateBlog.blog_writer = request.POST['writer']
    updateBlog.blog_body = request.POST['body']
    updateBlog.blog_date = timezone.now()
    updateBlog.save()
    return redirect('detailOne',updateBlog.id)


def deleteOne(request, blog_id):
    deleteBlog =  Blog.objects.get(id = blog_id)
    deleteBlog.delete()
    return redirect('homeOne')
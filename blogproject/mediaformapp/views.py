from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import blogForm

# Create your views here.

def homeTwo(request):
    blog = Blog.objects.all()
    return render(request,'homeTwo.html',{'blog' : blog})

def detailTwo(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detailTwo.html' ,{'blog' : blog_detail})

def newTwo(request):
    if request.method == 'POST': #폼 다채우고 저장버튼 눌렀을 때
        form = blogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.blog_date = timezone.now()
            post.save()
            return redirect('detailTwo', post.id)
        return redirect('homeTwo')
    else:  #글을 쓰기위해 들어갔을 때
        form = blogForm()
        return render(request,'newTwo.html', {'form':form})


def editTwo(request, blog_id):
    post = get_object_or_404(Blog, pk = blog_id)
    if request.method == 'GET':  #수정하려고 들어갔을 때
        form = blogForm(instance = post)
        return render(request, 'editTwo.html', {'form' : form})
    else:   #수정 끝나고 수정 버튼을 눌렀을 때
        form = blogForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            post = form.save(commit = False)
            post.blog_date = timezone.now()
            post.save()
            return redirect('/mediaformapp/detailTwo/' + str(blog_id))
        return redirect('homeTwo')

def deleteTwo(request, blog_id):
    deleteBlog =  Blog.objects.get(id = blog_id)
    deleteBlog.delete()
    return redirect('homeTwo')
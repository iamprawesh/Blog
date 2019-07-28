from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'blog/index.html',{'articles':articles})

def article_detail(request,slug):
    article = Article.objects.get(slug=slug)
    # return HttpResponse(slug)
    return render(request,'blog/detail.html',{'article':article})

@login_required(login_url ='/accounts/login/')
def create_post(request):
    if request.method == 'POST':
        form= forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            print(instance.author)
            form.save()
            instance.save()
            return redirect('blog:index')
    else:
        form = forms.CreateArticle()
    return render(request,'blog/create_post.html',{'form':form})
    # return HttpResponse("hello")
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import Article, Comment, Ip
from .forms import ArticleForm, CommentForm, UserSignUpForm

from .serializers import ArticleSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class ArticleApiView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    return render(request, 'main/index.html')

#account
def profile(request):
    if not request.user.is_authenticated:
        return redirect('sign_in')
    else:
        articles_model = Article.objects.filter(author = request.user)
        return render(request, 'main/profile.html', context = {'articles': articles_model})
        
def other_profile(request, username):
    articles_model = Article.objects.filter(author__username__contains = username)
    return render(request, 'main/profile.html', context = {'articles': articles_model})

def sign_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully!!!')
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'main/sign_in.html', {'form': form})
    else:
        return redirect('profile')


def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserSignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('sign_in')
        else:
            form = UserSignUpForm()
        return render(request, 'main/sign_up.html', {'form': form})
    
    else:
        return redirect('profile')

def sign_out(request):
    logout(request)
    return redirect('index')



#articles
def articles(request):
    articles_model = Article.objects.order_by('-date')
    return render(request, 'main/articles.html', context = {'articles': articles_model})

def articles_category(request, category_slug):
    articles_model = Article.objects.filter(category__slug=category_slug)
    return render(request, 'main/articles.html', context = {'articles': articles_model})

def article(request, article_slug):
    comments = Comment.objects.filter(article__slug=article_slug)
    article_object = get_object_or_404(Article, slug=article_slug)
    ip = get_client_ip(request)

    if Ip.objects.filter(ip=ip).exists():
        article_object.views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        article_object.views.add(Ip.objects.get(ip=ip))  

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.article = article_object
            form.save()
            return redirect('article', article_slug=article_slug)
    else:
        form = CommentForm() 
        return render(request, 'main/article.html', context={'article': article_object, 'form': form, 'comments': comments})



def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('index')
    else:
        form = ArticleForm() 
    return render(request, 'main/create_edit_article.html', context = {'form': form, 'title': 'Create article'})

def edit_article(request, article_slug):
    article_object = get_object_or_404(Article, slug=article_slug)
    if request.user == article_object.author:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article_object)
            if form.is_valid():
                form.save()
                return redirect('index')
            
        else:
            form = ArticleForm(instance=article_object)
            return render(request, 'main/create_edit_article.html', context = {'form': form, 'title': 'Edit article'})
    else: 
        return redirect('index')
def about_us(request):
    return render(request, 'main/about_us.html')

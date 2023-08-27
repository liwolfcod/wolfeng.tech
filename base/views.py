from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import BlogPost,ContactMessages
from . forms import BlogForm,ContactForm,CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

def Home(request):
    return render(request, 'Home.html')

def About(request):
    return render(request, 'About.html')

def Blog(request):
    blogposts = BlogPost.objects.all()
    p = Paginator(blogposts[::-1], 3)
    page_number = request.GET.get('page')
    try:
        pagination = p.get_page(page_number)
    except PageNotAnInteger:
        pagination = p.page(1)
    except EmptyPage:
        pagination = p.page(p.num_pages)
    print(pagination , blogposts)
    return render(request, 'Blog.html', {'BlogPosts':blogposts,'Pagination':pagination})

def BlogPage(request, pk):
    blog = BlogPost.objects.get(title=pk)
    context = {'blog': blog}
    return render(request, 'BlogPage.html', context)

def Contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm (request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, 'Contact.html', context)

def loginPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    context = {'form': form,}
    return render(request, 'Login.html', context)

def Logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def AddBlog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm (request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, 'Add_Blog.html', context)

@login_required(login_url='login')
def update_blog(request,pk):
    blog = BlogPost.objects.get(id=pk)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm (request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, 'Add_Blog.html', context)

@login_required(login_url='login')
def delete_blog(request,pk):
    blog = BlogPost.objects.get(id=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('dashboard')
    return render(request, 'Delete_Blog.html', {'obj':blog})

@login_required(login_url='login')
def delete_message(request,pk):
    message = ContactMessages.objects.get(id=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('messages')
    return render(request, 'Delete_Message.html', {'obj':message})

@login_required(login_url='login')
def AdminPanel(request):
    return render(request, 'AdminPanel.html')

@login_required(login_url='login')
def Dashboard(request):
    if request.method == "POST":
        q = request.POST['q']
        blog = BlogPost.objects.filter(title__contains=q)
        context = {'q': q, 'blog' : blog}
        return render(request, 'Dashboard.html', context)
    else:
        blog = BlogPost.objects.all()
        context = {'blog' : blog}
        return render(request, 'Dashboard.html', context)

@login_required(login_url='login')
def Messages(request):
    if request.method == "POST":
        q = request.POST['q']
        messages = ContactMessages.objects.filter(title__contains=q)
        context = {'q': q, 'messages' : messages}
        return render(request, 'Dashboard.html', context)
    else:
        messages = ContactMessages.objects.all()
        context = {'messages' : messages}
        return render(request, 'Messages.html', context)
    
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
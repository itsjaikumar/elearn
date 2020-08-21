from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    form = LessonForm()
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form,
    }
    return render(request, 'teach/index.html',context)

@login_required(login_url='login')
def home(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons':lessons,
    }
    return render(request, 'teach/home.html',context)

def registerPage(request):
    
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                
                messages.success(request, 'Account has been created for ' + username)
                return redirect('login')
        
        context ={'form':form}
        return render(request, 'teach/register.html', context)

def loginPage(request):
    
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'teach/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def updateLesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    form = LessonForm2(instance=lesson)

    if request.method == 'POST':
        form = LessonForm2(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {
        'form':form,
    }
    return render(request, 'teach/update_lesson.html', context)

def deleteLesson(request, pk):
    item = Lesson.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {
        'item':item,
    }
    return render(request, 'teach/delete.html', context)


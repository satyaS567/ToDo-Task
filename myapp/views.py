from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import Tasklist
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        obj = Tasklist.objects.all().filter(user=request.user)
        context ={
            'tasks':obj
        }
        return render(request,'home.html',context)
    else:
        return redirect('/')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:

        return render(request,'register.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('register')
    else:
        return redirect('register')
    
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            try:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                user = authenticate(username=username,password=password)
                login(request,user)
                return redirect('/')
            except Exception as e:
                return redirect('register')
        
        else:
            return redirect('register')
    else:
        return redirect('register')

def signout(request):
    logout(request)
    return redirect('register')

def addtask(request):
    if request.method=='POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        user = Tasklist(user=request.user,title=title,description=description,date=date)
        user.save()
        return redirect('/')
    else:
        return redirect('/')
    
def delete(request,id):
    task = Tasklist.objects.get(id=id)
    task.delete()
    return redirect('/')
    
def edit(request,id):
    task = Tasklist.objects.get(id=id)
    if request.method == 'POST':
        new_title = request.POST['title']
        new_description = request.POST['description']
        new_date = request.POST['date']

        task.title = new_title
        task.description = new_description
        task.date = new_date
        task.save()
        return redirect('/')
    return render(request,'edit.html',context={'tasks':task})
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employe

# Create your views here.
def index(request):
    return render(request,"index.html")
def  signup(request):
    if request.method =="POST":
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if not username or not password:
            messages.error(request,"username and password required")
            return render(request,"signup.html")

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request,"username taken")
                return render(request, "signup.html")
            else:
                user =User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('/signin')
        else:
            messages.error(request,"password doesnot match")
            return render(request,'signup.html')

    return render(request,"signup.html")
def  signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'home1.html')
        else:
            messages.error(request,"invalid username or password")
            return  redirect('signin')
    return render(request,"signin.html")

def add(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        post = request.POST['post']
        salary = request.POST['salary']
        employe = Employe(
            name=first_name,
            last_name=last_name,
            age=age,
            post=post,
            salary=salary
            )
        employe.save()
        return redirect("/view")
    return render(request,"add_employe.html")
def view(request):
    emp_list=Employe.objects.all()
    return render(request,"view.html",{'emp_list':emp_list})

def update(request,emp_id):
    emp1=Employe.objects.get(id=emp_id)
    if request.method == 'POST':
        emp1.name=request.POST['name']
        emp1.last_name = request.POST['last_name']
        emp1.age = request.POST['age']
        emp1.post = request.POST['post']
        emp1.salary = request.POST['salary']
        emp1.save()
        return redirect('/view')
    return render(request,'update.html',{'emp':emp1})
def delete(request,emp_id):
    emp1=Employe.objects.get(id=emp_id)
    emp1.delete()
    return redirect('/view')
def home(request):
    return render(request,'home1.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

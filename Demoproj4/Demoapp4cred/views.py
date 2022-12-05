from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        pwd = request.POST['pwd']
        user = auth.authenticate(username=username, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials. Check again or register.")
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pwd = request.POST['pwd']
        cpwd = request.POST['cpwd']
        if pwd == cpwd:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken. Try another name.")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email ID taken. Try another email.")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=pwd, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                messages.info(request, "New User Added.")
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match. Re-enter password")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
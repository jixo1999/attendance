from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    classrooms = Classroom.objects.all()
    trainers = Trainer.objects.all()
    context = {
        'classrooms': classrooms,
        'trainers': trainers,
    }
    return render(request, 'index.html', context)


def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        error_message = None
        user = None
        email = request.POST['email']
        pass1 = request.POST['pwd1']
        pass2 = request.POST['pwd2']
        if pass1 != pass2:
            error_message = "passwords didn't match!!"
            context = {'error_message': error_message}
            return render(request, 'index.html', context)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            error_message = "user doesn't exist!!"
            context = {'error_message': error_message}
            return render(request, 'index.html', context)
        user_auth = authenticate(username=user.username, password=pass1)
        if user_auth is not None:
            login(request, user_auth)
            return redirect('home')
        else:
            error_message = "incorrect password!!"
            context = {'error_message': error_message}
            return render(request, 'index.html', context)
    return render(request, 'index.html')


def Logout(request):
    logout(request)
    return redirect('login')

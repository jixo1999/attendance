from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import PasswordResetForm

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


class CustomPasswordResetView(PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'password_reset.html'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        # Add your custom logic to check if the email exists in the database
        if not User.objects.filter(email=email).exists():
            # Email doesn't exist, handle the error as desired (e.g., show an error message)
            return render(self.request, 'password_reset.html', {'error': 'Email does not exist.','form':PasswordResetForm})

        return super().form_valid(form)
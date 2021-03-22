from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.INFO, 'Username taken')
                return redirect('accounts:register')
            elif User.objects.filter(email=email).exists():
                messages.add_message(request, messages.INFO, 'Email taken')
                return redirect('accounts:register')
            else: 
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1
                )
                user.save()
                return redirect('hospital:index')
        else:
            messages.add_message(request, messages.INFO, "Password doesn't match")
    return render(request, 'accounts/register.html')


def login(request):
    return render(request, 'accounts/login.html')
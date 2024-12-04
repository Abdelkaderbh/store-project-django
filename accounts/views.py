from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use!")
            return redirect('register')

        user = User.objects.create_user(email=email, password=password)
        login(request, user)
        return redirect('dashboard')  # Replace with your store homepage

    return render(request, 'accounts/register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Replace with your store homepage
        else:
            messages.error(request, "Invalid email or password!")

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Replace with your login page

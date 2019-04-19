from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        #Sign up the USER
        if request.POST['inputPassword'] == request.POST['confirmPassword']:
            try:
                user = User.objects.get(username=request.POST['inputUsername'])
                return render(request, 'accounts/signup.html', {'error': 'Sorry! This username has already been taken.'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['inputUsername'], email=request.POST['inputEmail'], password=request.POST['inputPassword'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Sorry! The passwords must match.'})
    else:
        #User needs the form
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        #Sign up the USER
        user = auth.authenticate(username=request.POST['inputUsername'], password=request.POST['inputPassword'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Sorry! The username or password is incorrect.'})
    else:
        #User needs the form
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    #don't forget to logout
    return render(request, 'accounts/signup.html')

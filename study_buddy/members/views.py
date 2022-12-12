from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from study_buddy.members.forms import ProfileCreateForm


def index_no_account(request):
    return render(request, 'index_login_register.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out!")
    return redirect('index no_account')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, "There was an error logging in, Try again...")
            return redirect('login user')

    else:
        return render(request, 'users/sign_in.html')


def register_user(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('index')
    else:
        form = ProfileCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'users/sign_up.html', context)


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from templates_advanced.pythons_auth.forms import SignInForm


def sign_up(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign in')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'auth/sign-up.html', context)


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignInForm()

    context = {
        'form': form,
    }

    return render(request, 'auth/sign-in.html', context)

    # user = authenticate(username='biba', password='1234')
    # login(request, user)
    # return redirect('index')


def sign_out(request):
    logout(request)
    return redirect('index')


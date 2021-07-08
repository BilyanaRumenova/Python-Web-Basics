from django.shortcuts import render, redirect

from expence_tracker_2.common.budget import calculate_budget_left
from expence_tracker_2.expenses_app.models import Expense
from expence_tracker_2.profile_app.forms import ProfileForm, DeleteProfileForm
from expence_tracker_2.profile_app.models import Profile


def home_profile(request):
    profile = Profile.objects.all()[0]
    expenses = Expense.objects.all()

    profile.budget_left = calculate_budget_left(profile, expenses)

    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileForm()
        context = {
            'form': form
        }
        return render(request, 'home-no-profile.html', context)
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

        context = {
            'form': form
        }
        return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.all()[0]
    if request.method == 'GET':
        form = ProfileForm(instance=profile)
        context = {
            'form': form
        }
        return render(request, 'profile-edit.html', context)
    else:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home profile')

        context = {
            'form': form
        }
        return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.all()[0]
    if request.method == 'GET':
        return render(request, 'profile-delete.html')
    else:
        profile.delete()
        Expense.objects.all().delete()
        return redirect('home page')




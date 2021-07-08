from django.shortcuts import render, redirect

from notes_app.note_app.models import Note
from notes_app.profile_app.forms import ProfileForm
from notes_app.profile_app.models import Profile


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


def profile_details(request):
    profile = Profile.objects.all()[0]
    notes = Note.objects.all()

    context = {
        'profile': profile,
        'notes': notes,

    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = Profile.objects.all()[0]
    profile.delete()
    Note.objects.all().delete()
    return redirect('home page')

from django.shortcuts import render, redirect

from notes_app.note_app.forms import NoteForm, DeleteNoteForm
from notes_app.note_app.models import Note
from notes_app.profile_app.models import Profile
from notes_app.profile_app.views import create_profile


def home_page(request):
    if Profile.objects.exists():
        profile = Profile.objects.all()[0]
        notes = Note.objects.all()

        context = {
            'profile': profile,
            'notes': notes
        }
        return render(request, 'home-with-profile.html', context)

    else:
        return create_profile(request)


def add_note(request):
    if request.method == 'GET':
        form = NoteForm()
        context = {
            'form': form
        }
        return render(request, 'note-create.html', context)
    else:
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

        context = {
            'form': form
        }
        return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        form = NoteForm(instance=note)
        context = {
            'note': note,
            'form': form
        }
        return render(request, 'note-edit.html', context)
    else:
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')

        context = {
            'note': note,
            'form': form
        }
        return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        form = DeleteNoteForm(instance=note)
        context = {
            'note': note,
            'form': form
        }
        return render(request, 'note-delete.html', context)
    else:
        note.delete()
        return redirect('home page')


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note
    }
    return render(request, 'note-details.html', context)







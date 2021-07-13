from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import PetForm, EditPetForm
from petstagram.pets.models import Pet, Like


def list_pets(request):
    all_pets = Pet.objects.all()
    context = {
        'pets': all_pets
    }
    return render(request, 'pets/pet_list.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()

    context = {
        'pet': pet,
        'comment_form': CommentForm(),
        'comments': pet.comment_set.all()
    }
    return render(request, 'pets/pet_detail.html', context)


def comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = Comment(
            comment=form.cleaned_data['comment'],
            pet=pet
        )
        comment.save()

    return redirect('pet details', pet.id)


def like_pet(request, pk):
    pet_to_like = Pet.objects.get(pk=pk)
    like = Like(pet=pet_to_like)
    like.save()
    return redirect('pet details', pet_to_like.id)


def create_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list pets')

    else:
        form = PetForm()

    context = {
        'form': form,
    }
    return render(request, 'pets/pet_create.html', context)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('list pets')

    else:
        form = EditPetForm(instance=pet)

    context = {
        'form': form,
        'pet': pet
    }
    return render(request, 'pets/pet_edit.html', context)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('list pets')
    else:
        context = {
            'pet': pet
        }
        return render(request, 'pets/pet_delete.html', context)



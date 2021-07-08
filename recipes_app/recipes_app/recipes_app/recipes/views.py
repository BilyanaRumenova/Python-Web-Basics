from django.shortcuts import render, redirect


from recipes_app.recipes.forms import  DeleteRecipeForm, CreateRecipeForm, EditRecipeForm
from recipes_app.recipes.models import Recipe


def home_page(request):

    if Recipe.objects.exists():
        recipes = Recipe.objects.all()
        context = {
            'recipes': recipes
        }
        return render(request, 'index.html', context)
    else:

        return render(request, 'index.html')


# def home_page(request):
#     recipe = get_recipe()
#     if not recipe:
#         return render(request, 'index.html')
#
#     context = {
#         'recipes': recipe
#     }
#     return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'GET':
        form = CreateRecipeForm()
        context = {
            'form': form,
        }
        return render(request, 'create.html', context)
    else:
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

        context = {
            'form': form,
        }
        return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'recipe': recipe,
            'form': EditRecipeForm(instance=recipe)
        }
        return render(request, 'edit.html', context)
    else:
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')

        context = {
            'recipe': recipe,
            'form': form
        }
        return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'recipe': recipe,
            'form': DeleteRecipeForm(instance=recipe)
        }
        return render(request, 'delete.html', context)
    else:
        recipe.delete()
        return redirect('home page')


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(',')
    context = {
        'recipe': recipe,
        'ingredients': ingredients
    }
    return render(request, 'details.html', context)


def details_recipe_edit(request, pk):
    edit_recipe(request, pk)
    return redirect('edit recipe')


def details_recipe_delete(request, pk):
    delete_recipe(request, pk)
    return redirect('delete recipe')

from recipes_app.recipes.models import Recipe


def get_recipe():
    return Recipe.objects.all()
from django import forms

from recipes_app.common.common import DisabledFormMixin
from recipes_app.recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

        labels = {
            'title': 'Title',
            'image_url': 'Image URL',
            'description': 'Description',
            'ingredients': 'Ingredients',
            'time': 'Time (Minutes)',
        }


class CreateRecipeForm(RecipeForm):
    pass


class EditRecipeForm(RecipeForm):
    pass


class DeleteRecipeForm(RecipeForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
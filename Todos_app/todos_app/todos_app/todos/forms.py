from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from todos_app.todos.models import Todo
from todos_app.todos.validators import validate_owner_todos_count, validate_dot


def validate_bot_catcher_empty(value):
    if value:
        raise ValidationError('You are a bot!')


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        # fields = '__all__'
        # fields = ('title', 'state', 'description', 'owner')
        exclude = ('categories',)
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter todo text'
                },
            ),
            'owner': forms.RadioSelect()
        }

    def clean(self):
        validate_owner_todos_count(self.cleaned_data['owner'])

    # def clean_title(self):
    #     validate_dot(self.cleaned_data['title'])


class CreateTodoForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        # validators=[
        #     MinValueValidator(3)
        # ],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter todo text',
            }
        )
    )
    # state = forms.BooleanField()
    description = forms.CharField(
        max_length=20,
        widget=forms.Textarea(
            attrs= {
                'class': 'my-text-area',
                'rows': 3,
                'placeholder': 'Enter todo description',
            }
        ),
    )

    bots_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
        validators=[
            # validate_bot_catcher_empty,
        ]
    )

    def clean_bot_catcher(self):
        value = self.cleaned_data['bots_catcher']
        validate_bot_catcher_empty(value)


class UpdateTodoForm(CreateTodoForm):
    state = forms.BooleanField


class DeleteTodoForm(CreateTodoForm):
    pass



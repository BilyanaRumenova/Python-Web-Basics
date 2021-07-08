from django.shortcuts import render

from todos_app.forms_workshop.user_form import UserForm


def show_form_data(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            fields = ['name', 'age', 'email', 'password', 'text']
            [print(field, form.cleaned_data[field]) for field in fields]
        else:
            print(form.errors)

    else:
        context = {
            'form': UserForm(),
        }
        return render(request, 'forms_workshop/../../templates/forms_workshop/../../templates/todo_app/create.html', context)


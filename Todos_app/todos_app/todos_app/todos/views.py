from django.shortcuts import render, redirect

from todos_app.todos.forms import CreateTodoForm, UpdateTodoForm, DeleteTodoForm, TodoForm
from todos_app.todos.models import Todo
from todos_app.todos.models.todo import Person


# def index(request):
#     context = {
#         'todos': Todo.objects.all(),
#         'form': CreateTodoForm()
#     }
#     return render(request, 'index.html', context)
#
#
# def create_todo(request):
#     form = CreateTodoForm(request.POST)
#
#     if form.is_valid():
#         text = form.changed_data['text']
#         description = form.cleaned_data['description']
#         todo = Todo(
#             text=text,
#             description=description,
#             # owner=owner
#         )
#         todo.save()
#         return redirect('/')
#     else:
#         context = {
#             'todos': Todo.objects.all(),
#             'form': form
#         }
#         return render(request, 'index.html', context)
#
#
# def change_todo_state(request, pk):
#     todo = Todo.objects.get(pk=pk)
#     todo.state = not todo.state
#     todo.save()
#     return redirect('/')

def index(request):
    context = {
        'todos': Todo.objects.all(),
    }
    return render(request, 'todo_app/index.html', context)


def create_todo(request):
    form = TodoForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')


    context = {
        'form': form
    }
    return render(request, 'todo_app/create.html', context)


def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == "GET":
        context = {
            'form': TodoForm(initial=todo.__dict__)
        }
        return render(request, 'todo_app/edit.html', context)

    elif request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'form': form
            }

            return render(request, 'todo_app/edit.html', context)


# def delete_todo(request, pk):
#     todo = Todo.objects.get(pk=pk)
#
#     if request.method == "GET":
#         context = {
#             'form': TodoForm(initial=todo.__dict__)
#         }
#         return render(request, 'todo_app/edit.html', context)
#
#     elif request.method == 'POST':
#         form = TodoForm(request.POST, instance=todo)
#
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#         else:
#             context = {
#                 'form': form
#             }
#
#             return render(request, 'todo_app/edit.html', context)

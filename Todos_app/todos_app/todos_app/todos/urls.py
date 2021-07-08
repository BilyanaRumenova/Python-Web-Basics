from django.urls import path

from todos_app.todos.views import index, create_todo, update_todo
urlpatterns = [
    path('', index),
    path('create/', create_todo, name='create_todo'),
    path('update/<int:pk>', update_todo, name='update_todo'),
    # path('delete/<int:pk>', delete_todo, name='delete_todo'),
    # # path('todos-add/', create_todo),
    # path('todo-change-state/<int:pk>', change_todo_state)
]
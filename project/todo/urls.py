from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.index, name="index"),
    path("done/<int:pk>/", views.todo_done, name="todo_done"),
    path("undo/<int:pk>/", views.todo_undo, name="todo_undo"),
    path("delete/<int:pk>/", views.todo_delete, name="todo_delete"),
]

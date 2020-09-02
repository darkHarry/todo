from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.index, name="index"),
    path("done/<int:pk>/", views.todo_done, name="todo_done"),
    path("undo/<int:pk>/", views.todo_undo, name="todo_undo"),
    path("delete/<int:pk>/", views.todo_delete, name="todo_delete"),
    path("api/todos/", views.todo_list, name="todo_list"),
    path("api/todos/<int:pk>/", views.todo_detail, name="todo_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.index, name="index"),
    path("check/<int:pk>/", views.todo_check, name="todo_done"),
    path("delete/<int:pk>/", views.todo_delete, name="todo_delete"),
    path("api/todos/", views.todo_list, name="todo_list"),
    path("api/todos/<int:pk>/", views.todo_detail, name="todo_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

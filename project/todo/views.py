from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse

from .models import Todo
from .forms import AddTodoForm, EditTodoForm
from .serializers import TodoSerializer


# display all todos
def index(request):
    if request.method == "POST":
        form = AddTodoForm(request.POST)
        if form.is_valid():
            new_todo = Todo()
            new_todo.todo_text = form.cleaned_data["new_todo"]
            new_todo.save()
            return HttpResponseRedirect(reverse("todo:index"))
    elif request.method == "GET":
        form = AddTodoForm()

    todos = Todo.objects.all().order_by("-pk")
    todo_forms = [EditTodoForm(instance=todo) for todo in todos]
    todo_list = list(zip(todos, todo_forms))
    context = {
        "form": form,
        "todo_list": todo_list,
    }
    return render(request, "todo/index.html", context)


# to check a todo
def todo_check(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.todo_done = not todo.todo_done
    todo.save()
    return HttpResponseRedirect(reverse("todo:index"))


# to delete a todo
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return HttpResponseRedirect(reverse("todo:index"))


@csrf_exempt
@api_view(["GET", "POST"])
def todo_list(request, format=None):
    if request.method == "GET":
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["GET", "PUT", "DELETE"])
def todo_detail(request, pk, format=None):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "GET":
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

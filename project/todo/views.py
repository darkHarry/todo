from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.urls import reverse

from .models import Todo
from .forms import AddTodoForm
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
    context = {
        "form": form,
        "todo_list": todos,
    }
    return render(request, "todo/index.html", context)


# to checkout a todo
def todo_done(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.todo_done = True
    todo.save()
    return HttpResponseRedirect(reverse("todo:index"))


# to uncheck a todo
def todo_undo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.todo_done = False
    todo.save()
    return HttpResponseRedirect(reverse("todo:index"))


# to delete a todo
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return HttpResponseRedirect(reverse("todo:index"))


@csrf_exempt
def todo_list(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "GET":
        serializer = TodoSerializer(todo)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = TodoSerializer(todo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        todo.delete()
        return HttpResponse(status=204)

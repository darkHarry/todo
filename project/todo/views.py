from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Todo
from .forms import AddTodoForm

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

    todos = Todo.objects.all()
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

# HttpResponse return a response to the user
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo


# New todo_list function that handle the request
# tell Django to use it when the client goes to a specifi URL with
# by default, Django looks at directly to template folder inside the app, todo in this case

# Print out all todos in HTML files
# pass another parameter in a render method is with [context]
# context is a dictionary with a key and a value
def todo_list(request):
    todos = Todo.objects.all()
    context = {
        "todo_list": todos
    }
    return render(request, "todo_list.html", context)


# CRUD - Create Retrieve, Update, Delete, List

def todo_detail(request, id):
    # Get a specific instance of id
    todo = Todo.objects.get(id=id)
    context = {
        "todo": todo
    }
    return render(request, "todo_detail.html", context)


def todo_create(request):
    # Create an instance of the form
    form = TodoForm(request.POST or None)
    if form.is_valid():
        # Django knows how to save the fields with the from model
        form.save()
        return redirect('/')
        # Don't need to create this code bellow - form model doing this already:
        # name = form.cleaned_data['name']
        # due_date = form.cleaned_data['due_date']
        # print(name, due_date)

        # # if form is valid, create a todo object
        # new_todo = Todo.objects.create(name=name, due_date=due_date)
        # pass
    context = {"form": form}
    return render(request, "todo_create.html", context)


def todo_update(request, id):
    # Get a specific instance of id
    todo = Todo.objects.get(id=id)

    # Create an instance of the form with instance=todo
    # instance=todo pass the data into the form and pre-populate the fields related to the model
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, "todo_update.html", context)


def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')

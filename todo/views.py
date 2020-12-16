from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_todo_list(request):
    # Gets a query set of all the items in the DB
    items = Item.objects.all()
    # A dictionary with our items in
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    # Create an instance of the form
    form = ItemForm()
    # Create a context which contains the empty form
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)

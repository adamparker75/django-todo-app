from django.shortcuts import render, redirect, get_object_or_404
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


# The item_id is the one we attached to the edit link in the html template
def edit_item(request, item_id):
    # Gets an instance of the item model
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    # Pass an instance to the form which is the item from the DB
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')

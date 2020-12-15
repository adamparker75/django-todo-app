from django.shortcuts import render
from .models import Item

# Create your views here.


def get_todo_list(request):
    # Gets a query set of all the items in the DB
    items = Item.objects.all()
    # A dictionary with our items in
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)

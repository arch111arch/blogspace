from django.shortcuts import render
from .models import Item

# Create your views here.
# Views are how the user comunicates from the frontend to the backend webpages.

#def say_hello(request):
#    return HttpResponse("<h1>Things I need to do</h1>")

def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


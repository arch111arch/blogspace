from django.shortcuts import render, redirect
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

def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')

def open_page(request):
    return render(request, 'todo/open_page.html')

def home(request):
    items = Item.objects.all()  
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)

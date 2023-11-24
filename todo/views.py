from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


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
       form = ItemForm(request.POST)
       if form.is_valid():
        form.save()
        #checks if the data is ok and saves the form.
        return redirect('get_todo_list')
            #name = request.POST.get('item_name')
            #done = 'done' in request.POST
            #Item.objects.create(name=name, done=done)
        #the ItemForm creates the form instead.
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)

def edit_item(request, item_id):
    #get a copy of the database
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
       form = ItemForm(request.POST, instance=item)
       if form.is_valid():
        form.save()
        return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }

    return render(request, 'todo/edit_item.html', context)


def open_page(request):
    return render(request, 'todo/open_page.html')

def home(request):
    items = Item.objects.all()  
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)

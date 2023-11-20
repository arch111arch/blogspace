from django.shortcuts import render, HttpResponse

# Create your views here.
# Views are how the user comunicates from the frontend to the backend webpages.

def say_hello(request):
    return HttpResponse("Hello!")
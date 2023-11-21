"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo.views import get_todo_list
from todo.views import open_page
from todo.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_todo_list, name='get_todo_list'),
    path('open', open_page, name='open_page'),
    path('home', home, name='home')
# takes 3 arguments.
#The path the user types in. The function that returns. A name for the path.
#'' empty string means our homepage.
]

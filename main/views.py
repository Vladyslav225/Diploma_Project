# Create your views here.

from django.shortcuts import render
from django.shortcuts import render, redirect

from .forms import TaskForm, LoginForm
from .models import Task, Catalogue



def home(reqests):
    task = Task.objects.order_by('title') # Sorting by a certain field

    return render(reqests, 'home.html', {'task': task})


def about(request):
    return render(request, 'about.html')


def catalogue(request):
    prod = Catalogue.objects.order_by() # Sorting by a certain field

    return render(request, 'catalogue.html', {'prod': prod})


def basket(request):
    return render(request, 'basket.html')


def opinions(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            error = 'Созданная форма неверная'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'opinions.html', context)


def login(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            error = 'Неверная регистрация'

    form = LoginForm()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'login.html', context)
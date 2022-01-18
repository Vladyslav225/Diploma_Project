
  
from .models import Task, Login
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task

        fields = [
            'title',
            'task'
            ]

        widgets = {
            'title': TextInput(
                attrs = {
                'class': 'form-control',
                'placeholder': 'Имя'
                }),
            'task': Textarea(
                attrs = {
                'class': 'form-control',
                'placeholder': 'Отзыв'
                })
            }

class LoginForm(ModelForm):
    class Meta:
        model = Login
        
        fields = [
            'name',
            'email'
            ]

        widgets = {
            'name': TextInput(
                attrs = {
                'class': 'form-control',
                'placeholder': 'Введите имя'
                }),
            'email': TextInput(
                attrs = {
                'class': 'form-control',
                'placeholder': 'Введите email'
                })
            }
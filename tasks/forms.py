from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from django.utils import timezone

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "status"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter task title"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Task details..."}),
            "due_date": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"},
                format="%Y-%m-%dT%H:%M"
            ),
            "status": forms.Select(attrs={"class": "form-control"}),
        }
    
    def clean_due_date(self):
        due_date = self.cleaned_data["due_date"]
        if due_date < timezone.now():
            raise forms.ValidationError("Due date cannot be in the past!")
        return due_date


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text="Required. Enter a valid email address.",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email"})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Choose a username"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter password"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm password"}),
        }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
34

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        exclude = ["user", "slug"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "picture": forms.FileInput(attrs={"class": "form-control"}),
            "emp_id": forms.NumberInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            "address": forms.Textarea(attrs={"class": "form-control"}),
            "full_time": forms.Select(attrs={"class": "form-control"}),
            "designation": forms.TextInput(attrs={"class": "form-control"}),
            "salary": forms.NumberInput(attrs={"class": "form-control"}),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "placeholder": "password",
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "placeholder": "password",
            }
        ),
    )
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        max_length=16, widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        fields = ["username", "password"]

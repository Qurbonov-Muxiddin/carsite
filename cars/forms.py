from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Car


class CarForm(forms.ModelForm):
    """Create va Update sahifalari uchun ModelForm (talab 4)"""

    class Meta:
        model = Car
        fields = ["brand", "name", "year", "price", "description", "image"]
        widgets = {
            "brand": forms.Select(attrs={"class": "form-select"}),
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Mashina nomi"}),
            "year": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Masalan: 2023"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Narxi (USD)"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


class RegisterForm(UserCreationForm):
    """Ro'yxatdan o'tish formasi (talab 1)"""
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})

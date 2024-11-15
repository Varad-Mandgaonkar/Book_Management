from django import forms
from .models import Book  # Import the Book model from models.py

class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # The model associated with this form
        fields = ['title', 'author', 'genre']  # List of fields to include in the form
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter genre'}),
        }

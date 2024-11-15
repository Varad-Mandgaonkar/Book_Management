# library/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # List all books
    path('create/', views.create_book, name='create_book'),  # Create a new book
    path('update/<int:pk>/', views.update_book, name='update_book'),  # Update an existing book
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),  # Delete a book
]


from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

#Create your views here

# Read - List all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

# Create - Add a new book
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/create_book.html', {'form': form})

# Update - Edit an existing book
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/update_book.html', {'form': form})

# Delete - Remove a book
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'library/delete_book.html', {'book': book})

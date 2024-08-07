from django.shortcuts import render
from .models import BookModel
from django.views.generic import ListView,DetailView
# Create your views here.
class BookListView(ListView):
    queryset = BookModel.objects.all()
    template_name = 'browse/browse_book.html'
    
class BookDetailView(DetailView):
    model = BookModel
    template_name = 'book_detail.html'

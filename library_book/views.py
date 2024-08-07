from typing import Any
from django.shortcuts import render
from .models import BookModel,BookReview
from django.views.generic import ListView,DetailView
# Create your views here.
class BookListView(ListView):
    queryset = BookModel.objects.all()
    template_name = 'browse/browse_book.html'
    
class BookDetailView(DetailView):
    model = BookModel
    template_name = 'browse/book_detail.html'
    context_object_name = 'book'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = BookReview.objects.filter(book=self.object)
        return context

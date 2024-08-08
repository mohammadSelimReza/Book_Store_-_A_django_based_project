from typing import Any
from django.shortcuts import render,redirect,get_object_or_404
from .models import BookModel,BookReview
from library_book.models import CategoryModel
from django.views.generic import ListView,DetailView
from .forms import ReviewForm
# Create your views here.
class BookListView(ListView):
    template_name = 'browse/browse_book.html'
    context_object_name = 'bookmodel_list'
    
    def get_queryset(self):
        queryset = BookModel.objects.all()
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        return context
    
class BookDetailView(DetailView):
    model = BookModel
    template_name = 'browse/book_detail.html'
    context_object_name = 'book'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.review.all()
        if self.request.method == 'POST':
            comment_form = ReviewForm(data=self.request.POST)
            if comment_form.is_valid():
                new_comment=comment_form.save(commit=False)
                new_comment.post = post
                new_comment.save()
                return redirect('bookDetail', pk=post.pk)
        else:
            comment_form = ReviewForm()
            
        context['review'] = comments
        context['comment_form'] = comment_form
        return context
 
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        book = self.object
        comment_form = ReviewForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            return redirect('bookDetail', slug=book.slug)
        return self.get(request, *args, **kwargs)           
    

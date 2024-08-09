from django.urls import path
from .views import BookListView,BookDetailView,BookReviewView

urlpatterns = [
    path('books/',BookListView.as_view(),name='bookList'),
    path('book/<slug:slug>/',BookDetailView.as_view(),name='bookDetail'),
    path('book/<int:book_id>/review/', BookReviewView.as_view(), name='review_book'),
]

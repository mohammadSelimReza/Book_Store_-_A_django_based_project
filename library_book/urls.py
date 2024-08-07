from django.urls import path
from .views import BookListView,BookDetailView

urlpatterns = [
    path('books/',BookListView.as_view(),name='bookList'),
    path('book/<slug:slug>/',BookDetailView.as_view(),name='bookDetail'),
]

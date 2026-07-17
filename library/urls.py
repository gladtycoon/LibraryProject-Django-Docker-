from django.urls import path
# from .views import books_list, books_detail
from .views import BookCreateView, BooksListView, BookUpdateView, BookDetailView, BookDeleteView, AuthorCreate, AuthorUpdate, AuthorListView, RecommendBookView, ReviewBookView

app_name = 'library'


urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='authors_list'),
    path('author/new/', AuthorCreate.as_view(), name='author_create'),
    path('author/update/<int:pk>/', AuthorCreate.as_view(), name='author_update'),

    # path('books_list/', books_list, name='books_list'),
    # path('book_detail/<int:book_id>', books_detail, name='book_detail'),
    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    path('books/recommend/<int:pk>/',RecommendBookView.as_view(), name='book_recommend'),
    path('books/review/<int:pk>/', ReviewBookView.as_view(), name='book_review'),
]
from django.urls import path
from .views import BookListCreate, BookRetrieveUpdateDestroy, checkout, return_book, CategoryListCreate, CategoryRetrieveUpdateDestroy, UserListCreate, TransactionList

urlpatterns = [
    # Books
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-retrieve-update-destroy'),
    path('books/<int:pk>/checkout/', checkout, name='book-checkout'),
    path('books/<int:pk>/return/', return_book, name='book-return'),

    # Categories
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-retrieve-update-destroy'),

    # Users
    path('users/', UserListCreate.as_view(), name='user-list-create'),

    # Transactions
    path('transactions/', TransactionList.as_view(), name='transaction-list'),
]

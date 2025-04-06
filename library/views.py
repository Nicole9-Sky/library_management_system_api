from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Book, Category, User, Transaction
from .serializers import BookSerializer, CategorySerializer, UserSerializer, TransactionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics 
2
# Create yourfrom rest_framework import generics

# Views for Categories
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


# Views for Books (with Category included)
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


# Views for Transactions (Checkout and Return)
@api_view(['POST'])
def checkout(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        if not book.available:
            return Response({'error': 'Book is already checked out'}, status=status.HTTP_400_BAD_REQUEST)
        book.available = False
        book.save()

        # Create a transaction entry for the checkout
        Transaction.objects.create(book=book, user=request.user, action='checkout')

        return Response({'message': 'Book checked out successfully'}, status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def return_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        if book.available:
            return Response({'error': 'Book was not checked out'}, status=status.HTTP_400_BAD_REQUEST)
        book.available = True
        book.save()

        # Create a transaction entry for the return
        Transaction.objects.create(book=book, user=request.user, action='return')

        return Response({'message': 'Book returned successfully'}, status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)


# User View
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


# Transaction View
class TransactionList(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AllowAny]

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from books_api.models import Book
from books_api.serializers import BookSerializer


class BookListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookGetUpdateDelete(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, book_id):
        try:
            book = Book.objects.get(pk=book_id)
            book_serializer = BookSerializer(book)
            return Response(book_serializer.data)
        except:
            return Response({'message': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, book_id):
        try:
            book = Book.objects.get(pk=book_id)
            book_serializer = BookSerializer(book, data=request.data)
            if book_serializer.is_valid():
                book_serializer.save()
                return Response(book_serializer.data, status=status.HTTP_200_OK)
            return Response(book_serializer.errors)
        except:
            return Response({'message': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, book_id):
        try:
            book = Book.objects.get(pk=book_id)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'message': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
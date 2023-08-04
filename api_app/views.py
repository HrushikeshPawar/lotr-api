from django.http import JsonResponse
from .models import Book, Chapter, Character, Movie, Quote
from .serializers import BookSerializer, ChapterSerializer, CharacterSerializer, MovieSerializer, QuoteSerializer
from rest_framework.decorators import api_view
from rest_framework import status



@api_view(['GET'])
def get_book_list(request):

    # Get all the books from the database
    books = Book.objects.all()

    # Serialize the data
    serializer = BookSerializer(books, many=True)

    # Return the serialized data
    return JsonResponse({'books': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_book_by_id(request, book_id):

    # Get the book from the database
    # Check if the book exists
    try:
        book = Book.objects.get(book_id=book_id)
    except Book.DoesNotExist:
        return JsonResponse({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Serialize the data
    serializer = BookSerializer(book)

    # Return the serialized data
    return JsonResponse({'book': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_chapter_list(request):

    # Get all the chapters from the database
    chapters = Chapter.objects.all()

    # Serialize the data
    serializer = ChapterSerializer(chapters, many=True)

    # Return the serialized data
    return JsonResponse({'chapters': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_chapter_by_id(request, chapter_id):
    
        # Get the chapter from the database
        # Check if the chapter exists
        try:
            chapter = Chapter.objects.get(chapter_id=chapter_id)
        except Chapter.DoesNotExist:
            return JsonResponse({'message': 'The chapter does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
        # Serialize the data
        serializer = ChapterSerializer(chapter)
    
        # Return the serialized data
        return JsonResponse({'chapter': serializer.data}, status=status.HTTP_200_OK)


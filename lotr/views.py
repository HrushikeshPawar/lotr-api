from django.http import JsonResponse
from rest_framework import status

# Welcome message
def welcome(request):
    message = """Welcome to the Lord of the Rings API. To use the API, please use the following endpoints:
    /api/books
    /api/books/<book_id>
    /api/chapters
    /api/chapters/<chapter_id>
    /api/characters
    /api/characters/<character_id>
    /api/movies
    /api/movies/<movie_id>
    /api/quotes
    /api/quotes/<quote_id>
    """
    return JsonResponse({'message': message}, status=status.HTTP_200_OK)


# API info
def api_info(request):

    message = """This API is a collection of data from the Lord of the Rings books and movies."""
    return JsonResponse({'message': message, 'verion': 1}, status=status.HTTP_200_OK)
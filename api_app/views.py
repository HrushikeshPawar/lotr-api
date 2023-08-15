from django.http import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .models import Book, Chapter, Character, Movie, Quote
from .serializers import BookSerializer, ChapterSerializer, CharacterSerializer, MovieSerializer, QuoteSerializer, UserSerializer


## Views rwequired for the user authentication
# Register a new user
@api_view(['POST'])
def register_user(request):
    # Get the data from the request
    serializer = UserSerializer(data=request.data)

    # Check if the data is valid
    if serializer.is_valid():

        # Save the user to the database
        serializer.save()

        # Get the user from the database
        user = User.objects.get(username=serializer.data['username'])

        # Hash the password
        user.set_password(user.password)

        # Save the user again
        user.save()

        # Create a token for the user
        token = Token.objects.create(user=user)

        # Return user data and token
        return JsonResponse({'user': serializer.data, 'token': token.key}, status=status.HTTP_201_CREATED)

    # Return the error message if the data is not valid
    return JsonResponse({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# Login a user, to get the token
@api_view(['POST'])
def login_user(request):

    # Get the user
    user = get_object_or_404(User, username=request.data['username'])

    # Check if the password is correct
    if not user.check_password(request.data['password']):
        return JsonResponse({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    # Get the token for the user
    token, created = Token.objects.get_or_create(user=user)

    # Return the user data and token
    return JsonResponse({'user': UserSerializer(instance=user).data, 'token': token.key}, status=status.HTTP_200_OK)

###

## The views for the API

# Get all the books
@api_view(['GET'])
def get_book_list(request):

    # Get all the books from the database
    books = Book.objects.all()

    # Serialize the data
    serializer = BookSerializer(books, many=True)

    # Return the serialized data
    return JsonResponse({'books': serializer.data}, status=status.HTTP_200_OK)


# Get a book by id
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


# Get all the characters from LoTR, requires authentication
@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_chapter_list(request):

    # Get all the chapters from the database
    chapters = Chapter.objects.all()

    # Serialize the data
    serializer = ChapterSerializer(chapters, many=True)

    # Return the serialized data
    return JsonResponse({'chapters': serializer.data}, status=status.HTTP_200_OK)


# Get a chapter by id, requires authentication
@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
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


# Get all the characters from LoTR, requires authentication
@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_character_list(request):

    # Get all the characters from the database
    characters = Character.objects.all()

    # Serialize the data
    serializer = CharacterSerializer(characters, many=True)

    # Return the serialized data
    return JsonResponse({'characters': serializer.data}, status=status.HTTP_200_OK)


# Get a character by id, requires authentication
@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_character_by_id(request, character_id):

    ## Get the character from the database
    # Check if the character exists
    try:
        character = Character.objects.get(character_id=character_id)
    except Character.DoesNotExist:
        return JsonResponse({'message': 'The character does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Serialize the data
    serializer = CharacterSerializer(character)

    # Return the serialized data
    return JsonResponse({'character': serializer.data}, status=status.HTTP_200_OK)


# Get all the movies from LoTR, requires authentication
@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_movie_list(request):

    # Get all the movies from the database
    movies = Movie.objects.all()

    # Serialize the data
    serializer = MovieSerializer(movies, many=True)

    # Return the serialized data
    return JsonResponse({'movies': serializer.data}, status=status.HTTP_200_OK)


# Get a movie by id, requires authentication
@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_movie_by_id(request, movie_id):

    ## Get the movie from the database
    # Check if the movie exists
    try:
        movie = Movie.objects.get(movie_id=movie_id)
    except Movie.DoesNotExist:
        return JsonResponse({'message': 'The movie does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Serialize the data
    serializer = MovieSerializer(movie)

    # Return the serialized data
    return JsonResponse({'movie': serializer.data}, status=status.HTTP_200_OK)

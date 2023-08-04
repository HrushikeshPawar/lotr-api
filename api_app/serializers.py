from rest_framework.serializers import ModelSerializer
from .models import Book, Chapter, Character, Movie, Quote
from django.contrib.auth.models import User


# The Book Serializer
class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


# The Chapter Serializer
class ChapterSerializer(ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'


# The Character Serializer
class CharacterSerializer(ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


# The Movie Serializer
class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


# The Quote Serializer
class QuoteSerializer(ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


# The User Serializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
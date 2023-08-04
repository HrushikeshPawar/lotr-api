from django.db import models

# Create your models here.
class Book(models.Model):

    book_id = models.CharField(primary_key=True, max_length=255)
    book_name = models.CharField(max_length=255)

    def __str__(self):
        return self.book_name


class Chapter(models.Model):

    chapter_id = models.CharField(primary_key=True, max_length=255)
    chapter_name = models.CharField(max_length=255)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, to_field='book_id')

    def __str__(self):
        return self.chapter_name


class Character(models.Model):

    character_id = models.CharField(primary_key=True, max_length=255)
    character_name = models.CharField(max_length=255)
    character_race = models.CharField(max_length=255)
    character_gender = models.CharField(max_length=255)
    character_birth = models.CharField(max_length=255)
    character_death = models.CharField(max_length=255)
    character_hair = models.CharField(max_length=255)
    character_height = models.CharField(max_length=255)
    character_relam = models.CharField(max_length=255)
    character_spouse = models.CharField(max_length=255)
    character_wikiurl = models.CharField(max_length=255)

    def __str__(self):
        return self.character_name


class Movie(models.Model):
    # name,runtimeInMinutes,budgetInMillions,boxOfficeRevenueInMillions,academyAwardNominations,academyAwardWins,rottenTomatoesScore,_id
    movie_id = models.CharField(primary_key=True, max_length=255)
    movie_name = models.CharField(max_length=255)
    movie_runtimeInMinutes = models.IntegerField()
    movie_budgetInMillions = models.IntegerField()
    movie_boxOfficeRevenueInMillions = models.FloatField()
    movie_academyAwardNominations = models.IntegerField()
    movie_academyAwardWins = models.IntegerField()
    movie_rottenTomatoesScore = models.FloatField()

    def __str__(self):
        return self.movie_name


class Quote(models.Model):
    # dialog,movie,character,_id
    quote_id = models.CharField(primary_key=True, max_length=255)
    quote_dialog = models.CharField(max_length=1024)
    quote_movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, to_field='movie_id')
    quote_character_id = models.ForeignKey(Character, on_delete=models.CASCADE, to_field='character_id')

    def __str__(self):
        return self.quote_dialog

from api_app.models import Book, Chapter, Character, Movie, Quote
import csv
import os
from tqdm.auto import tqdm


# Create new Book objects from csv
def create_Books(csv_file):

    # Open the csv
    with open(csv_file) as file:
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # Delete all records in the Book table
        Book.objects.all().delete()

        # Create a new Book object for each row in the csv
        #   Assumes the columns are in the order of your models
        for row in tqdm(reader, desc="Creating Books"):
            Book.objects.create(
                book_id=row[1],
                book_name=row[0],
            )


# Create new Chapter objects from csv
def create_Chapters(csv_file):

    # Open the csv
    with open(csv_file) as file:
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # Delete all records in the Chapter table
        Chapter.objects.all().delete()

        # Create a new Chapter object for each row in the csv
        #   Assumes the columns are in the order of your models
        for row in tqdm(reader, desc="Creating Chapters"):
            Chapter.objects.create(
                chapter_name=row[0],
                book_id=Book.objects.get(book_id=row[1]),
                chapter_id=row[2],
            )


# Create new Character objects from csv
def create_Characters(csv_file):

    with open(csv_file) as file:
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # Delete all records in the Chapter table
        Character.objects.all().delete()

        # Create a new Chapter object for each row in the csv
        #   Assumes the columns are in the order of your models
        for row in tqdm(reader, desc="Creating Characters"):
            Character.objects.create(
                character_name = row[0],
                character_wikiurl = row[1],
                character_race = row[2],
                character_birth = row[3],
                character_gender = row[4],
                character_death = row[5],
                character_hair = row[6],
                character_height = row[7],
                character_relam = row[8],
                character_spouse = row[9],
                character_id = row[10],
            )


# Create new Movie objects from csv
def create_Movies(csv_file):

    with open(csv_file) as file:
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # Delete all records in the Chapter table
        Movie.objects.all().delete()

        # Create a new Chapter object for each row in the csv
        #   Assumes the columns are in the order of your models
        for row in tqdm(reader, desc="Creating Movies"):
            Movie.objects.create(
                movie_name = row[0],
                movie_runtimeInMinutes = row[1],
                movie_budgetInMillions = row[2],
                movie_boxOfficeRevenueInMillions = row[3],
                movie_academyAwardNominations = row[4],
                movie_academyAwardWins = row[5],
                movie_rottenTomatoesScore = row[6],
                movie_id = row[7],
            )


# Create new Quote objects from csv
def create_Quotes(csv_file):

    with open(csv_file) as file:
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # Delete all records in the Chapter table
        Quote.objects.all().delete()

        # Create a new Chapter object for each row in the csv
        #   Assumes the columns are in the order of your models
        for row in tqdm(reader, desc="Creating Quotes"):
            Quote.objects.create(
                quote_dialog = row[0],
                quote_movie_id = Movie.objects.get(movie_id=row[1]),
                quote_character_id = Character.objects.get(character_id=row[2]),
                quote_id = row[3],
            )


def run():
    print(f"Loading `books.csv` data into database...")
    csv_file = os.path.join('db', 'csv', 'books.csv')
    create_Books(csv_file)
    print('Books loaded!')

    print(f"\nLoading `chapters.csv` data into database...")
    csv_file = os.path.join('db', 'csv', 'chapters.csv')
    create_Chapters(csv_file)
    print('Chapters loaded!')

    print(f"\nLoading `characters.csv` data into database...")
    csv_file = os.path.join('db', 'csv', 'characters.csv')
    create_Characters(csv_file)
    print('Characters loaded!')

    print(f"\nLoading `movies.csv` data into database...")
    csv_file = os.path.join('db', 'csv', 'movies.csv')
    create_Movies(csv_file)
    print('Movies loaded!')

    print(f"\nLoading `quotes.csv` data into database...")
    csv_file = os.path.join('db', 'csv', 'quotes.csv')
    create_Quotes(csv_file)
    print('Quotes loaded!')
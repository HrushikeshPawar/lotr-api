from django.contrib import admin
from .models import Book, Chapter, Character, Movie, Quote

# Register your models here.
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Character)
admin.site.register(Movie)
admin.site.register(Quote)
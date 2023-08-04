from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_user),
    path('login', views.login_user),
    path('books', views.get_book_list),
    path('book/<str:book_id>', views.get_book_by_id),
    path('chapters', views.get_chapter_list),
    path('chapter/<str:chapter_id>', views.get_chapter_by_id),
    path('characters', views.get_character_list),
    path('character/<str:character_id>', views.get_character_by_id),
]
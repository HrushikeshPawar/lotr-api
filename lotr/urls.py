"""
URL configuration for lotr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api_app import views

urlpatterns = [
    path('register', views.register_user),
    path('login', views.login_user),
    path('books', views.get_book_list),
    path('book/<str:book_id>', views.get_book_by_id),
    path('chapters', views.get_chapter_list),
    path('chapter/<str:chapter_id>', views.get_chapter_by_id),
    path('characters', views.get_character_list),
    path('character/<str:character_id>', views.get_character_by_id),
    path('movies', views.get_movie_list),
    path('movie/<str:movie_id>', views.get_movie_by_id),
    path('quotes', views.get_quote_list),
    path('quote/<str:quote_id>', views.get_quote_by_id),
]

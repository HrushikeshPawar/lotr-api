# Generated by Django 4.2.4 on 2023-08-04 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('character_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('character_name', models.CharField(max_length=255)),
                ('character_race', models.CharField(max_length=255)),
                ('character_gender', models.CharField(max_length=255)),
                ('character_birth', models.CharField(max_length=255)),
                ('character_death', models.CharField(max_length=255)),
                ('character_hair', models.CharField(max_length=255)),
                ('character_height', models.CharField(max_length=255)),
                ('character_relam', models.CharField(max_length=255)),
                ('character_spouse', models.CharField(max_length=255)),
                ('character_wikiurl', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=255)),
                ('movie_runtimeInMinutes', models.IntegerField()),
                ('movie_budgetInMillions', models.IntegerField()),
                ('movie_boxOfficeRevenueInMillions', models.FloatField()),
                ('movie_academyAwardNominations', models.IntegerField()),
                ('movie_academyAwardWins', models.IntegerField()),
                ('movie_rottenTomatoesScore', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('quote_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('quote_dialog', models.CharField(max_length=255)),
                ('quote_character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.character')),
                ('quote_movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('chapter_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('chapter_name', models.CharField(max_length=255)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.book')),
            ],
        ),
    ]

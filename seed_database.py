"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb ratings")
# More code will go here

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
    # Movie.query.all()
    title = movie['title']
    overview = movie['overview']
    poster_path = movie['poster_path']
    release_date = datetime.strptime(movie['release_date'], "%Y-%m-%d")
    # TODO: create a movie here and append it to movies_in_db
    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)


model.db.session.add_all(movies_in_db)
model.db.session.commit()

users_in_db = []
for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    # TODO: create a user here
    db_user = crud.create_user(email, password)
    model.db.session.add(db_user)
    users_in_db.append(db_user)
    # TODO: create 10 ratings for the user
    
    num_ratings = 0
    ratings_in_db = []
    while num_ratings <= 10:
        rating = randint(0,5)
        movie_to_review = choice(movies_in_db)
        rating_created = crud.create_rating(db_user, movie_to_review, rating)
        ratings_in_db.append(rating_created)
        num_ratings += 1
    model.db.session.add_all(ratings_in_db)

model.db.session.commit()   
        
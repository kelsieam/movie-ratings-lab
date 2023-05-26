"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


# Functions start here!
def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user




def create_movie(title, overview, release_date, poster_path):

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    return movie


def create_rating(user, movie, score):

    # user1 = User.query.get(1)
    # movie1 = Movie.query.get(1)
    # rating1 = Rating(user=user1, movie=movie1, score=score)

    rating = Rating(user=user, movie=movie, score=score) # user=User Object, movie=Movie Object

    return rating

# def create_rating_2(user_id, movie_id, score):

#     rating = Rating(user_id=user_id, movie_id=movie_id, score=score)

#     return rating

def all_the_movies():
    all_movies = Movie.query.all()
    return all_movies


def get_movie_by_id(movie_id):
    #### working on this
    selected_movie = Movie.query.filter(Movie.movie_id == movie_id).one()
    return selected_movie

def get_user_by_id(user_id):
    #### working on this
    selected_user = User.query.filter(User.user_id == user_id).one()
    return selected_user

def all_the_users():
    all_users = User.query.all()
    return all_users

def get_user_by_email(email):
    user_email = User.query.filter(User.email == email)
    return user_email

def create_user(email, password):
    user = User(email=email, password=password)
    return user

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
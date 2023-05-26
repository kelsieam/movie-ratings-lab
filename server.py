"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/movies')
def movies():
    movies = crud.all_the_movies()
    return render_template("all_movies.html", movies = movies)

@app.route('/movies/<movie_id>')
def movie_details(movie_id):
    movie=crud.get_movie_by_id()
    return render_template("movie_details.html", movie = movie)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

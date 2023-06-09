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
    movie = crud.get_movie_by_id(movie_id)
    return render_template("movie_details.html", movie = movie)

@app.route('/users')
def users():
    users = crud.all_the_users()
    return render_template("all_users.html", users=users)

@app.route('/users/<user_id>')
def user_details(user_id):
    user = crud.get_user_by_id(user_id)
    return render_template("user_details.html", user = user)

@app.route('/users', methods =['POST'] )
def register_user():
    email = request.form.get('email')
    password = request.form.get('password')

    check_email = crud.get_user_by_email(email)
    print(check_email)
    if check_email is not None:
        flash("You can't use that email")

    else:
        new_user = crud.create_user(email, password)
        flash("Your account has been created")
        db.session.add(new_user)
        db.session.commit()

    return redirect('/')


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

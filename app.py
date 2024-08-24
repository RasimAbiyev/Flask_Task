from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345@localhost/kino_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    released = db.Column(db.String(50))
    director = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50))

with app.app_context():
    db.create_all()

with app.app_context():
    movies = [
        Movie(title="Inception", released="2010", director="Christopher Nolan", genre="Sci-Fi"),
        Movie(title="The Dark Knight", released="2008", director="Christopher Nolan", genre="Action"),
        Movie(title="Pulp Fiction", released="1994", director="Quentin Tarantino", genre="Crime"),
        Movie(title="The Godfather", released="1972", director="Francis Ford Coppola", genre="Crime"),
        Movie(title="Forrest Gump", released="1994", director="Robert Zemeckis", genre="Drama"),
        Movie(title="The Matrix", released="1999", director="Lana Wachowski, Lilly Wachowski", genre="Sci-Fi")
    ]
    db.session.bulk_save_objects(movies)
    db.session.commit()

@app.route('/movies/')
def movie_list():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

@app.route('/movies/<int:movie_id>')
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template('movie.html', movie=movie)

if __name__ == '__main__':
    app.run(debug=True)

from flask import render_template, redirect, request, abort, url_for, jsonify
from models import Movies, Animations, Serials
from form import MovieForm, AnimationForm, SerialForm, BaseMediaForm
from ext import app, dataBase



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return {"status": "ok"}



@app.route("/api/movies")
def api_movies():
    movies = Movies.query.all()
    movies_list = [{
        "name": movie.name,
        "image": movie.image,
        "date": movie.date,
        "genre": movie.genre,
        "director": movie.director,
        "description": movie.description,
        "actors": movie.actors
    } for movie in movies]
    return movies_list


@app.route("/api/movies/name/<string:name>")
def get_movie_by_name(name):
    movie = Movies.query.filter_by(name=name).first()
    if not movie:
        return {"error": "Movie not found"}, 404
    return jsonify({
        "name": movie.name,
        "image": movie.image,
        "date": movie.date,
        "genre": movie.genre,
        "director": movie.director,
        "description": movie.description,
        "actors": movie.actors
    })


@app.route("/api/animations")
def api_animations():
    animations = Animations.query.all()
    animations_list = [{
        "name": animation.name,
        "image": animation.image,
        "date": animation.date,
        "genre": animation.genre,
        "director": animation.director,
        "description": animation.description,
        "actors": animation.actors
    } for animation in animations]
    return animations_list

@app.route("/api/animations/name/<string:name>")
def get_animation_by_name(name):
    animation = Animations.query.filter_by(name=name).first()
    if not animation:
        return {"error": "Animation not found"}, 404
    return jsonify({
        "name": animation.name,
        "image": animation.image,
        "date": animation.date,
        "genre": animation.genre,
        "director": animation.director,
        "description": animation.description,
        "actors": animation.actors
    })


@app.route("/api/serials")
def api_serials():
    serials = Serials.query.all()
    serials_list = [{
        "name": serial.name,
        "image": serial.image,
        "date": serial.date,
        "genre": serial.genre,
        "director": serial.director,
        "description": serial.description,
        "actors": serial.actors
    } for serial in serials]
    return serials_list


@app.route("/api/serials/name/<string:name>")
def get_serial_by_name(name):
    serial = Serials.query.filter_by(name=name).first()
    if not serial:
        return {"error": "Serial not found"}, 404
    return jsonify({
        "name": serial.name,
        "image": serial.image,
        "date": serial.date,
        "genre": serial.genre,
        "director": serial.director,
        "description": serial.description,
        "actors": serial.actors
    })



@app.route("/add/<media_type>", methods=["GET", "POST"])
def add_media(media_type):
    form_map = {
        "movie": MovieForm,
        "animation": AnimationForm,
        "serial": SerialForm
    }

    model_map = {
        "movie": Movies,
        "animation": Animations,
        "serial": Serials
    }

    redirect_map = {
        "movie": "movies",
        "animation": "animations",
        "serial": "serials"
    }

    form = form_map.get(media_type)
    model = model_map.get(media_type)

    if not form or not model:
        abort(404)

    form = form()

    if form.validate_on_submit():
        item = model()
        form.populate_obj(item)
        dataBase.session.add(item)
        dataBase.session.commit()

        return redirect(url_for(redirect_map[media_type]))

    return render_template("mediaForm.html", form=form, title=f"Add {media_type.capitalize()}")



@app.route("/Movies")
def movies():
    movies = Movies.query.all()
    return render_template("movies.html", movies=movies)

@app.route("/Animations")
def animations():
    animations = Animations.query.all()
    return render_template("animations.html", animations=animations)

@app.route("/Serials")
def serials():
    serials = Serials.query.all()
    return render_template("serials.html", serials=serials)


@app.route("/delete/<media_type>/<int:id>")
def delete_media(media_type, id):
    model_map = {
        "movie": Movies, 
        "animation": Animations, 
        "serial": Serials
        }
    
    item = model_map[media_type].query.get_or_404(id)
    dataBase.session.delete(item)
    dataBase.session.commit()
    return redirect(request.referrer or f"/{media_type}s")


@app.route("/edit/<media_type>/<int:id>", methods=["GET", "POST"])
def edit_media(media_type, id):
    model_map = {
        "movie": Movies,
        "animation": Animations,
        "serial": Serials
    }

    redirect_map = {
        "movie": "movies",
        "animation": "animations",
        "serial": "serials"
    }

    model = model_map.get(media_type)
    if not model:
        abort(404)

    item = model.query.get_or_404(id)
    form = BaseMediaForm(obj=item)

    if form.validate_on_submit():
        form.populate_obj(item)
        dataBase.session.commit()

        return redirect(url_for(redirect_map[media_type]))

    return render_template("mediaForm.html", form=form, title=f"Edit {media_type.capitalize()}")
    


if __name__ == "__main__":
    app.run(debug=True)
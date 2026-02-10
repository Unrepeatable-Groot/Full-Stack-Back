from ext import dataBase

class Movies(dataBase.Model):
    __tablename__ = "movies"

    id = dataBase.Column(dataBase.Integer(), primary_key=True)
    name = dataBase.Column(dataBase.String())
    image = dataBase.Column(dataBase.String())
    date = dataBase.Column(dataBase.Integer())
    genre = dataBase.Column(dataBase.String())
    director = dataBase.Column(dataBase.String())
    description = dataBase.Column(dataBase.String())
    actors = dataBase.Column(dataBase.String())

class Animations(dataBase.Model):
    __tablename__ = "animations"

    id = dataBase.Column(dataBase.Integer(), primary_key=True)
    name = dataBase.Column(dataBase.String())
    image = dataBase.Column(dataBase.String())
    date = dataBase.Column(dataBase.Integer())
    genre = dataBase.Column(dataBase.String())
    director = dataBase.Column(dataBase.String())
    description = dataBase.Column(dataBase.String())
    actors = dataBase.Column(dataBase.String())

class Serials(dataBase.Model):
    __tablename__ = "serials"
    
    id = dataBase.Column(dataBase.Integer(), primary_key=True)
    name = dataBase.Column(dataBase.String())
    image = dataBase.Column(dataBase.String())
    date = dataBase.Column(dataBase.Integer())
    genre = dataBase.Column(dataBase.String())
    director = dataBase.Column(dataBase.String())
    description = dataBase.Column(dataBase.String())
    actors = dataBase.Column(dataBase.String())

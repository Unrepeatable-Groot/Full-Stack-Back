from ext import app, dataBase
from models import Movies, Serials, Animations

with app.app_context():
    dataBase.create_all()
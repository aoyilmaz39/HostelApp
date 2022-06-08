from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
x=os.getcwd()[2:]
x=x.replace("\\","/")
x=x+"/Motel.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+x
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Odalik(db.Model):

    __abstract__ = True

    kisi = db.Column(db.Integer, primary_key=True)
    odanumarasi = db.Column(db.Integer)
    isimsoyisim = db.Column(db.String(50))
    telefon = db.Column(db.Integer)
    tc = db.Column(db.Integer)
    mail = db.Column(db.String(120))
    cinsiyet = db.Column(db.String(120))
    gtarih = db.Column(db.String(120))
    dtarih = db.Column(db.String(120))
    ctarih = db.Column(db.String(120))
    thesap = db.Column(db.Integer)
    odamasraf = db.Column(db.String(10000))
    bitti = db.Column(db.Boolean)

class Satis(db.Model):

    sira = db.Column(db.Integer, primary_key=True)
    urun=db.Column(db.String(120), unique=True)
    fiyati=db.Column(db.Integer)

class Odafiyat(db.Model):

    siralik = db.Column(db.Integer, primary_key=True)
    odalar = db.Column(db.String(120), unique=True)
    fiyat = db.Column(db.Integer)

class Oda1(Odalik):
    __tablename__ = 'Oda1'

class Oda2(Odalik):
    __tablename__ = 'Oda2'

class Oda3(Odalik):
    __tablename__ = 'Oda3'

class Oda4(Odalik):
    __tablename__ = 'Oda4'

class Oda5(Odalik):
    __tablename__ = 'Oda5'

class Oda6(Odalik):
    __tablename__ = 'Oda6'

class Oda7(Odalik):
    __tablename__ = 'Oda7'

class Oda8(Odalik):
    __tablename__ = 'Oda8'

class Oda9(Odalik):
    __tablename__ = 'Oda9'

class Oda10(Odalik):
    __tablename__ = 'Oda10'

class Oda11(Odalik):
    __tablename__ = 'Oda11'

class Oda12(Odalik):
    __tablename__ = 'Oda12'

class Oda13(Odalik):
    __tablename__ = 'Oda13'

class Oda14(Odalik):
    __tablename__ = 'Oda14'

class Gecmis(Odalik):
    __tablename__ = "Gecmis"


if __name__=="__main__":
    db.create_all()
    app.run(debug=True)

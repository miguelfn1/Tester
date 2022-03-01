from email.policy import default
from xmlrpc.client import DateTime
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy
from src.server.instance import server
from src.controllers.restaurantes import *
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)

class Pessoa(db.Model):
    __tablename__= 'usuario'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    restaurante = db.Column(db.String)
    horario = db.Column(db.DateTime)

    def __init__ (self, nome, restaurante, horario):
        self.nome = nome
        self.restaurante = restaurante
        self.horario = horario

db.create_all()

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        restaurante = request.form.get("restaurante")
        horario = datetime.now()

        if nome and restaurante and  horario:

            p = Pessoa(nome,restaurante,horario)
            #if horario.hour >= 9 and horario.hour <= 11 and horario.minute <= 50:
            db.session.add(p)
            db.session.commit()
            #else:
               # return 'Votação Já encerrada !'


    return redirect(url_for("index"))  

@app.route("/lista")
def lista():
   pessoas  = Pessoa.query.all()
   return render_template('lista.html', pessoas=pessoas )
        
        
if __name__=='__main__':
    app.run(debug=True)

server.run()
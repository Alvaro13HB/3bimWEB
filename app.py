from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = '6955c2b0a51d2b8035b9b0df8fc34b3550ddea153d7d46821f339d1f3712f2fc'

conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/3bim_db"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from database import db
from flask_migrate import Migrate
from models import Usuario, Pizza, PDiddy

db.init_app(app)
migrate = Migrate(app, db)

from modules.usuarios.usuarios import bp_usuario
app.register_blueprint(bp_usuario, url_prefix='/usuarios')

from modules.pizzas.pizzas import bp_pizzas
app.register_blueprint(bp_pizzas, url_prefix='/pizzas')
from flask import Blueprint, render_template, request, redirect, flash
from models import Pdiddy
from database import db

bp_pdiddy = Blueprint('pdiddys', __name__, template_folder="templates")

@bp_pdiddy.route('/')
def index():
    u = Pdiddy.query.all()
    return render_template("pdiddy.html", dados=u)


@bp_pdiddy.route('/add')
def add():
    return render_template("pdiddy_add.html")


@bp_pdiddy.route('/save', methods=['POST'])
def save():
    id_usuario = request.form.get('id_usuario')
    id_pizza = request.form.get('id_pizza')
    data = request.form.get('data')
    if id_usuario and id_pizza and data:
        db_pdiddy = Pdiddy(id_usuario, id_pizza, data)
        db.session.add(db_pdiddy)
        db.session.commit()
        flash("Pedido cadastrado com sucesso!!!")
        return redirect('/pdiddys')
    else:
        flash("Preencha todos os campos!!!")
        return redirect('/pdiddys/add')
from database import db


class Usuario(db.Model):
    __tablename__ = 'tb_usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(200))


    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


    def __repr__(self):
        return f"<Usuario {self.nome}>"


class Pizza(db.Model):
    __tablename__ = 'tb_pizza'
    id = db.Column(db.Integer, primary_key=True)
    sabor = db.Column(db.String(100))
    ingredientes = db.Column(db.String(100))
    preco = db.Column(db.Float(2, 10))


    def __init__(self, sabor, ingredientes, preco):
        self.sabor = sabor
        self.ingredientes = ingredientes
        self.preco = preco

    
    def __repr__(self):
        return f"<Pizza {self.sabor}>"
    

class PDiddy(db.Model):
    __tablename__ = 'tb_pdiddy'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('tb_usuario.id'))
    id_pizza = db.Column(db.Integer, db.ForeignKey('tb_pizza.id'))
    data = db.Column(db.Date)

    usuario = db.relationship('Usuario', foreign_keys=id_usuario)
    pizza = db.relationship('Pizza', foreign_keys=id_pizza)


    def __init__(self, id_usuario, id_pizza, data):
        self.id_usuario = id_usuario
        self.id_pizza = id_pizza
        self.data = data

    
    def __repr__(self):
        return f"<Pdiddy {self.usuario.nome} - {self.pizza.sabor} - {self.data}>"
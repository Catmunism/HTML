from db import db

class Projeto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(200))        # link para GitHub, Behance, etc.
    tecnologia = db.Column(db.String(100))  # ex: "HTML, CSS, Python"

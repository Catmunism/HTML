from flask import Flask, render_template, request, redirect, url_for
from db import db, init_db
from models import Projeto

app = Flask(__name__)
init_db(app)

# Criar tabelas na base de dados
with app.app_context():
    db.create_all()

# Página inicial: lista todos os projetos
@app.route("/")
@app.route("/home")
def home():
    projetos = Projeto.query.all()
    return render_template("home.html", projetos=projetos)

# Registar novo projeto
@app.route("/registar", methods=["GET", "POST"])
def registar():
    if request.method == "POST":
        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        link = request.form["link"]
        tecnologia = request.form["tecnologia"]

        novo_projeto = Projeto(
            titulo=titulo,
            descricao=descricao,
            link=link,
            tecnologia=tecnologia
        )

        db.session.add(novo_projeto)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("registar.html")

# Apagar projeto
@app.route("/apagar/<int:id>")
def apagar(id):
    projeto = Projeto.query.get_or_404(id)
    db.session.delete(projeto)
    db.session.commit()
    return redirect(url_for("home"))

# Editar projeto
@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    projeto = Projeto.query.get_or_404(id)

    if request.method == "POST":
        projeto.titulo = request.form["titulo"]
        projeto.descricao = request.form["descricao"]
        projeto.link = request.form["link"]
        projeto.tecnologia = request.form["tecnologia"]

        db.session.commit()
        return redirect(url_for("home"))

    return render_template("editar_projeto.html", projeto=projeto)

# Ver detalhes de um projeto
@app.route("/detalhe/<int:id>")
def detalhe(id):
    projeto = Projeto.query.get_or_404(id)
    return render_template("detalhe_projeto.html", projeto=projeto)

if __name__ == "__main__":
    app.run(debug=True)

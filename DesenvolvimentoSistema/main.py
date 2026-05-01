#coração do projeto, onde tudo se inicia

from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastro")
def fazer_conta():
    return render_template("cadastro.html")

@app.route("/entrar")
def entrar():
    return render_template("entrar.html")

@app.route("/contatar")
def contatar():
    return render_template("contatar.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/manutencao")
def manutencao():
    return render_template("manutencao.html")

@app.route("/paginaprincipal")
def pagina_principal():
    return render_template("paginaprincipal.html")

@app.route("/final")
def final():
    return render_template("final.html")

if __name__ == "__main__":
    app.run(debug=True)



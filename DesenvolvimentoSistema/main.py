#coração do projeto, onde tudo se inicia

from flask import Flask, render_template, request, redirect, url_for
import json
import os

def carregar_usuarios():
    if not os.path.exists("usuarios.json"):
        return []

    with open("usuarios.json", "r") as arquivo:
        return json.load(arquivo)

def salvar_usuario(novo_usuario):
    usuarios = carregar_usuarios()
    usuarios.append(novo_usuario)

    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo)

app = Flask(__name__)
#rota para a página inicial
@app.route("/")
def index():
    return render_template("index.html")



@app.route("/entrar", methods=["GET", "POST"])
def entrar():
    if request.method == "POST":
        # Aqui você pode processar os dados do formulário de login
        # Por exemplo, você pode obter os dados usando request.form['campo_nome']
        # E depois redirecionar para a página principal ou mostrar uma mensagem de sucesso
        email_digitado = request.form.get('email')
        senha_digitada = request.form.get('senha')

        # Carregamos a lista de quem já se cadastrou
        usuarios = carregar_usuarios()

        # Percorremos a lista procurando o e-mail e a senha
        email_encontrado = False
        erro = None
        for usuario in usuarios:
            if usuario['email'] == email_digitado:
                email_encontrado = True
                if usuario['senha'] == senha_digitada:
                    return redirect(url_for('pagina_principal'))
                else:
                    erro = "Senha errada, tente novamente"
                    return render_template("entrar.html", erro=erro)
        if not email_encontrado:
            erro = "Você não tem cadastro, faça seu cadastro primeiro"
            return render_template("entrar.html", erro=erro)
        # Se ele sair do loop e não achar nada, recarrega a página (ou mostra erro)
    return render_template("entrar.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro(): 
    if request.method == "POST":
        # Aqui você pode processar os dados do formulário de cadastro
        # Por exemplo, você pode obter os dados usando request.form['campo_nome']
        # E depois redirecionar para a página principal ou mostrar uma mensagem de sucesso
        nome = request.form.get('nome').title()
        email = request.form.get('email').lower()
        telefone = request.form.get('telefone')
        senha = request.form.get('senha')

        #dicionario temporario para armazenar os dados do usuario, usando json para simular um banco de dados, mais pra frente usaremos um banco de dados mais robusto, mas por enquanto isso é suficiente para o desenvolvimento inicial do sistema.
        novo_usuario = {
            "nome": nome,
            "email": email,
            "senha": senha 
        }

        #chamando a função para salvar o usuario no arquivo json, caso tudo tenha cido preenchido, volrara para o (pagina_principal) para confirmar os dados, caso contrário, permanecerá na página de entrar
        salvar_usuario(novo_usuario)

        #depois de salvar o usuario, verificamos se os dados foram preenchidos corretamente, caso contrário, permanecerá na página de entrar
        return redirect(url_for('entrar'))
        #caso tudo tenha cido preenchido, volrara para o (entra) para confirmar os dados, caso contrário, permanecerá na página de cadastro
        if nome and email and telefone and senha:
            return redirect(url_for('entrar'))
    return render_template("cadastro.html")

@app.route("/entre_em_contato")
def contatar():
    return render_template("contatar.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/manutencao")
def manutencao():
    return render_template("manutencao.html")

@app.route("/principal")
def pagina_principal():
    return render_template("pagina_principal.html")

@app.route("/privacidade")
def privacidade():
    return render_template("privacidade.html")

@app.route("/final")
def final():
    return render_template("final.html")


if __name__ == "__main__":
    app.run(debug=True)


#coração do projeto, onde tudo se inicia

from flask import Flask, render_template, request, redirect, url_for, session
from bancodedados import get_conexao

app = Flask(__name__)
app.secret_key = 'devfolio123'

app.config['SESION_COOKIE_SAMESITE'] = 'lax'
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
        email_digitado = request.form.get('email').lower()
        senha_digitada = request.form.get('senha')

        # Carregamos a lista de quem já se cadastrou, antes json agora SQLite
        conexao = get_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT * FROM usuarios WHERE email = ? AND senha = ?",
            (email_digitado, senha_digitada)
        )
        usuario = cursor.fetchone()
        print("usuario encontrado:", usuario)
        conexao.close()

        if usuario:
            session['usuario'] = email_digitado
            return redirect(url_for('pagina_principal'))
        else:
            erro = "Email ou senha incoretos"
            return render_template("entrar.html", erro=erro)
        # Se ele sair do loop e não achar nada, recarrega a página (ou mostra erro)
    return render_template("entrar.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro(): 
    if request.method == "POST":
        nome = request.form.get('nome').lower()
        email = request.form.get('email').lower()
        senha = request.form.get('senha')
        telefone = request.form.get('telefone')
        # print(nome, email, senha, telefone)
        # banco de dados foi mudado de json (json não é bem banco de dados) para SQLite.
        conexao = get_conexao()
        cursor = conexao.cursor()
        cursor.execute (
            "INSERT INTO usuarios (nome, email, senha, telefone) VALUES (?, ?, ?, ?)",
            (nome, email, senha, telefone)
        )
        conexao.commit()
        conexao.close()
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

@app.route("/pagina_principal")
def pagina_principal():
    conexao = get_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM projetos")
    projetos = cursor.fetchall()
    conexao.close()


    if 'usuario' in session:
        return render_template("pagina_principal.html", logado=True, projetos=projetos)
    else:
        return render_template("pagina_principal.html", logado=False, projetos=projetos)

@app.route("/criar_projeto", methods=["GET", "POST"])
def criar_projeto():
    if request.method == "POST":
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        linguagem = request.form.get('linguagem')
        autor_email = session['usuario']
        # banco
        conexao = get_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO projetos(titulo, descricao, linguagem, autor_email) VALUES (?, ?, ?, ?)",
            (titulo, descricao, linguagem, autor_email)
        )
        conexao.commit()
        conexao.close()
        return redirect(url_for('pagina_principal'))

    return render_template("criar_projeto.html")

@app.route("/privacidade")
def privacidade():
    return render_template("privacidade.html")

@app.route("/final")
def final():
    session.clear()
    return render_template("final.html")


if __name__ == "__main__":
        app.run(debug=True)


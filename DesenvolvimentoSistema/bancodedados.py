# banco de dados, onde serão armazenados os dados do site, como usuários, projetos, etc.
# por enquanto, estamos usando um arquivo JSON para simular um banco de dados simples, mas em um projeto real.
# você pode usar um banco de dados relacional como MySQL, PostgreSQL ou SQLite.

import sqlite3
def criar_banco():
    conexao = sqlite3.connect("devefolio.db")

    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            senha TEXT,
            telefone TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projetos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            descricao TEXT,
            linguagem TEXT,
            autor_email TEXT
        )
    ''')

    conexao.commit()
    conexao.close()

criar_banco()


def get_conexao():
    conexao = sqlite3.connect("devefolio.db")
    conexao.row_factory = sqlite3.Row
    return conexao


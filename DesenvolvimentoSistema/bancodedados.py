# banco de dados, onde serão armazenados os dados do site, como usuários, projetos, etc.
# por enquanto, estamos usando um arquivo JSON para simular um banco de dados simples, mas em um projeto real.
# você pode usar um banco de dados relacional como MySQL, PostgreSQL ou SQLite.

from flask import Flask, render_template, request, redirect, url_for
from main import app

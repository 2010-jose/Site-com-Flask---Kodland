from flask import Flask
import random

app = Flask(__name__)

fatos = [
    "O Sol é uma estrela.",
    "A água é composta por dois átomos de hidrogênio e um átomo de oxigênio.",
    "A Terra é o terceiro planeta do sistema solar.",
    "O corpo humano tem 206 ossos.",
    "A velocidade da luz é de aproximadamente 299.792.458 metros por segundo."
    "O cérebro humano é composto por cerca de 86 bilhões de neurônios.",
    "A gravidade é a força que atrai os objetos para o centro da Terra.",]

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

@app.route("/")
def hello_world():
    return '<h1>Página inicial</h1>' + '<a href="/random_fact"><h2>Veja um fato aleatório!</h2></a>' + '<br>' + '<a href="/gerador_de_senhas"><h2>Gerar uma senha aleatória</h2></a>'

@app.route("/random_fact") 
def random_fact():
    fato = random.choice(fatos)
    return f"<h1>Fato aleatório: {fato}</h1>"

@app.route("/gerador_de_senhas")
def gerador_de_senhas():
    senha = ""
    for i in range(10):
        carac = random.choice(caracteres)
        senha += carac
    return f"<h1>Senha gerada: {senha}</h1>"

app.run(debug=True)

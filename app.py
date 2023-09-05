from flask import Flask, render_template

app = Flask("meu app")

posts = [
    {"titulo": "Minha primeira postagem", "texto": "teste"},
    {"titulo": "Segundo Post", "texto": "outro teste"},
]

@app.route("/")
def exibir_entradas():
    entradas = posts  # Mock das postagens
    return render_template("exibir_entradas.html", entradas=entradas)

@app.route("/layout")
def layout ():
    return render_template("layout.html")

@app.route('/novo')
def novo():
    return "<h1> Nova Página</h1>"
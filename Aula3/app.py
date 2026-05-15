from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') 
def App():
    return render_template("index.html")

@app.route('/cotemig/<nome>') 
def nome(nome):
    return f"<h1>Ola {nome}! Bem-vindo ao cotemig</h1>"

if __name__ == '__main__':
    app.run(debug=True)
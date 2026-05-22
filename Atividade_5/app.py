from flask import Flask, request, render_template_string
app = Flask(__name__)

USUARIOS_PERMITIDOS = [
    {"usuario": "marcos", "senha": "cotemig2026"},
    {"usuario": "janaina", "senha": "cotemig2026"},
    {"usuario": "caio", "senha": "12400246"} 
]

def show_the_login_form():
    return render_template_string("""
        <h2>Login - Atividade 5</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário" required><br><br>
            <input type="password" name="senha" placeholder="Senha" required><br><br>
            <button type="submit">Entrar</button>
        </form>
    """)

def do_the_login():
    usuario_inserido = request.form.get('usuario')
    senha_inserida = request.form.get('senha')

    for credencial in USUARIOS_PERMITIDOS:
        if credencial["usuario"] == usuario_inserido and credencial["senha"] == senha_inserida:
            return f"<h1>Bem-vindo, {usuario_inserido}!</h1>"
            
    return "<h1>Login inválido</h1>"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)

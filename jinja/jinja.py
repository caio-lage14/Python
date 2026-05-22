from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    nome_usuario = "Caio"
    idade_usuario = 18

    dados_usuario = {
        "nome": "Ana", 
        "email": "ana@email.com"
    }

    lista_alunos = [
        {"nome": "Ana", "nota": 8.5},
        {"nome": "Pedro", "nota": 5.0},
        {"nome": "Lucas", "nota": 7.0},
        {"nome": "Mariana", "nota": 6.4}
    ]

   
    return render_template(
        'jinja.html', 
        nome=nome_usuario, 
        idade=idade_usuario, 
        usuario=dados_usuario, 
        alunos=lista_alunos
    )

if __name__ == '__main__':
    app.run(debug=True)

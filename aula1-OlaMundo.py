from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def ola_mundo():
    return 'Olá, Mundo!' # Isso é o que será retornado quando a rota '/' for acessada

@app.route('/hello') # Isso é outro decorator, mapeando a função abaixo para a rota '/hello'
def hello():
    return 'Hello, World!' # Isso é o que será retornado quando a rota '/hello' for acessada

@app.route('/decorator')
def decorator():
    return 'Um decorator é uma ferramenta que permite "embrulhar" uma função ' \
    'para adicionar novos comportamentos a ela sem alterar seu código original.        ' \
    'Para que serve: Serve para automatizar tarefas repetitivas, como verificar logins, registrar logs ou medir' \
    ' o tempo de execução, mantendo o código limpo.No Flask (@app.route): Ele funciona como um sinalizador que diz ao servidor:' \
    ' "Quando o usuário acessar este endereço (URL), execute esta função específica".'

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento

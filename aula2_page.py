from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo</title>
        </head>
        <body>
            <h1>Currículo</h1>

            <h2>Informações Pessoais</h2>
            <ul>
                <li><strong>Nome:</strong> Caio Luis Lage de Assis</li>  
                <li><strong>Email:</strong> 12400246@aluno.cotemig.com.br</li>
                <li><strong>Telefone:</strong> (31) 99435-7310</li>
            </ul>

            <h2>Experiência Profissional</h2>
            <ul>
                <li><strong>Empresa:</strong> None</li>
                <li><strong>Cargo:</strong> None</li>
                <li><strong>Período:</strong> None</li>
            </ul>
            <h2>Histórico escolar</h2>
            <ul>
                <li><strong>Escola:</strong> Santa Maria COREU</li>
                <li><strong>Ensino:</strong> Ensiono fundametal 1 e 2</li>
                <li><strong>Período:</strong> 2014 -> 2023</li>
            </ul>
            <ul>
                <li><strong>Escola:</strong> Cotemig</li>
                <li><strong>Ensino:</strong> Ensiono médio técnico</li>
                <li><strong>Período:</strong> 2024 -> 2026 (previsão de termino do curso)</li>
            </ul>
            <h2>Idiomas</h2>
            <ul>
                <li><strong>Idioma:</strong> Ingles</li>
                <li><strong>Escola:</strong> Influx</li>
                <li><strong>Nivel:</strong> Avançado</li>
            </ul>
            <ul>
                <li><strong>Idioma:</strong> Espanhol</li>
                <li><strong>Escola:</strong> Santa Maria COREU</li>
                <li><strong>Nivel:</strong> Intemediario</li>
            </ul>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

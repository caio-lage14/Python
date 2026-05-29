import math
from flask import render_template, request

def calcular():
    # Pegamos o primeiro número (que será o 'A' em Bhaskara)
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]

    # Operações que usam apenas o primeiro número
    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro"
            etapas = f"Não existe raiz real de {num1}."
        else:
            resultado = round(math.sqrt(num1), 4)
            etapas = f"√{num1}"
            
    # Operação de Bhaskara (precisa de num1, num2 e num3)
    elif operacao == "bhaskara":
        num2 = float(request.form.get("num2", 0))
        num3 = float(request.form.get("num3", 0))
        
        # num1 é o A, num2 é o B, num3 é o C
        a, b, c = num1, num2, num3
        
        if a == 0:
            resultado = "Erro"
            etapas = "O valor de 'A' não pode ser zero em uma equação de 2º grau."
        else:
            delta = (b ** 2) - (4 * a * c)
            if delta < 0:
                resultado = "Sem raízes reais"
                etapas = f"Delta é negativo (Δ = {round(delta, 4)}). Não existem raízes reais."
            elif delta == 0:
                x = -b / (2 * a)
                resultado = round(x, 4)
                etapas = f"Delta é zero (Δ = 0). Possui uma raiz real: X = {resultado}"
            else:
                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)
                resultado = f"X1 = {round(x1, 4)} | X2 = {round(x2, 4)}"
                etapas = f"Δ = {round(delta, 4)}"

    # Operações normais que usam dois números
    else:
        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultado="",
            )
        num2 = float(num2_valor)

        if operacao == "+":
            resultado = round(num1 + num2, 4)
            etapas = f"{num1} + {num2}"
        elif operacao == "-":
            resultado = round(num1 - num2, 4)   
            etapas = f"{num1} - {num2}" 
        elif operacao == "*":
            resultado = round(num1 * num2, 4)  
            etapas = f"{num1} * {num2}"
        elif operacao == "/":
            if num2 != 0:
                resultado = round(num1 / num2, 4)  
                etapas = f"{num1} / {num2}"
            else:
                resultado = "ERRO"
                etapas = "Não é possível dividir por zero."
        elif operacao == "**":
            resultado = round(num1 ** num2, 4)  
            etapas = f"{num1} ^ {num2}"
        elif operacao == "log":
            if num1 <= 0 or num2 <= 0 or num2 == 1:
                resultado = "ERRO"
                etapas = "Valores inválidos para o logaritmo."
            else:
                resultado = round(math.log(num1, num2), 4)
                etapas = f"log de {num1} na base {num2}"
        else:
            resultado = "Operação inválida"
            etapas = "A opção selecionada é inválida."
        
    return render_template("calculadora.html", etapas=etapas, resultado=resultado)

def calculadora_simples(num1, operador, num2):

    if operador == "+":
        print("O seu resultado é",num1 + num2)

    elif operador == "-":
        print("O seu resultado é",num1 - num2)

    elif operador == "*":
        print("O seu resultado é",num1 * num2)

    elif operador == "/":
        print("O seu resultado é",num1 / num2)

    #Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

    else:
        print("0")

num1 = float (input("Digite o primeiro número: "))

operador = str (input("Digite o operador lógico: adição = '+',subtração = '-', multiplicação = '*', divisão = '/' :"))

num2 = float (input("Digite o segundo número: "))

calculadora_simples(num1, operador, num2)
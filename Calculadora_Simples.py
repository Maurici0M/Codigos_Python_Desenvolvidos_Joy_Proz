def calculadora_simples(num1, operador, num2):

    if operador == "+":
        print(f"O resultado para {num1} {operador} {num2} =", num1 + num2)

    elif operador == "-":
        print(f"O resultado para {num1} {operador} {num2} =",num1 - num2)

    elif operador == "*":
        print(f"O resultado para {num1} {operador} {num2} =",num1 * num2)

    elif operador == "/":
        print(f"O resultado para {num1} {operador} {num2} =",num1 / num2)

    #Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

    else:
        print("0")

    print("Muito obrigado por utilizar a calculadora!")

num1 = float (input("Digite o primeiro número: "))

operador = str (input("Digite o operador lógico: adição = '+',subtração = '-', multiplicação = '*', divisão = '/' : "))

num2 = float (input("Digite o segundo número: "))

calculadora_simples(num1, operador, num2)
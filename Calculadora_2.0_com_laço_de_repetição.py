def calculadora_melhorada():

    operador = input("Digite o operador lógico: adição '+', subtração '-', multiplicação '*', divisão '/' ou digite '0' para sair. ")

    while operador != "0":

        num1 = float (input("Digite o primeiro número: "))
        
        num2 = float (input("Digite o segundo número: "))

        if operador == "+":
            resultado = float (num1) + float (num2)

        elif operador == "-":
            resultado = float (num1) - float (num2)
            
        elif operador == "*":
            resultado = float (num1) * float (num2)

        elif operador == "/":
            resultado = float (num1) / float (num2)

        else:
            print("Essa opção não existe!")

        
        print("O resultado é: ", resultado)

        print("______________________________________________________________________________________")

        operador = input("Digite o operador lógico: adição '+', subtração '-', multiplicação '*', divisão '/' ou digite '0' para sair.")

        if operador == "0":
            print("Você escolheu sair. Muito obrigado por utilizar a calculadora!")

calculadora_melhorada()

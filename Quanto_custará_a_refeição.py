comida = str (input("Qual a comida que você irá pedir? "))
print("Sua comida será:",comida)

valor_comida = 25

bebida = str (input("Qual o nome da bebida que você quer? "))
print("Sua bebida será:",bebida)
valor_bebida = 8

dinheiro = float (input("Quanto de dinheiro você tem disponível? Para números decimais, utilize o ponto '.' em ver de vírgula ','. "))

print("Você tem R$ ",dinheiro)

valor_refeicao = valor_bebida + valor_comida

troco = dinheiro - valor_comida - valor_bebida

print("A sua refeição de",comida,"com",bebida, "custará: R$",valor_refeicao)

if dinheiro > valor_refeicao:

    print("Aguarde, estamos precessando o seu pagamento...")

    print("Muito bem! O seu pagamento foi aprovado!")

    print("O seu troco é de: R$",troco)

    print("Muito obrigado por comprar conosco!")

    print("Tenha uma ótima refeição! ;)")

else:

    print("Aguarde, estamos processando o seu pagamento...")

    print("Ops! Parece que você não tem dinheiro suficiente.")

    print("Não se preocupe, você poderá utilizar outras formas de pagamento para acrescentar o valor restante.")

    print("Falta pagar: R$",valor_refeicao - dinheiro)
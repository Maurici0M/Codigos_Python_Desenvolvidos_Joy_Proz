def categoria_cnh(pessoas, rodas, peso):

    if rodas == 2 or rodas == 3:
        categoria = "A"
    elif rodas >= 4 and pessoas <= 8 and peso <= 3500:
        categoria = "B"
    elif rodas >= 4 and peso >= 3600 or peso <= 6000:
        categoria = "C"
    elif rodas >= 4 and pessoas > 8:
        categoria = "D"
    elif rodas >= 4 and peso > 6000:
        categoria = "E"
    else:
        categoria = "Algo saiu errado. Não consegui identificar a melhor CNH para você. Volte a tentar inserir os dados novamente."

    print("Legal! A categoria ideal da sua CNH foi Categoria:", categoria)

pessoas = int (input("Quantas pessoas você carregará no veículo? "))
rodas = int (input("Quantas rodas o veículo que você irá dirigir tem? "))
peso = float (input("Qual o peso aproximado do seu veículo? Digite somente números: "))

categoria_cnh(pessoas, rodas, peso)
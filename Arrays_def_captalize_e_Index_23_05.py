def personagens_naruto (array):
    achei = False

  # 1 - Criação do laço de repetição 'while' | 2 - e do 'input' de interação 'nome'.

    while (achei == False):
        nome = input("Digite o nome de um personagem de Naruto: ")

        captalize = nome.capitalize()   

#A variável que teve o nome "Captalize", traz uma função interessante, que deixará a primeira letra digitada em maiúscula.
#Assim, caso o usuário digite "naruto" em vez de "Naruto", ou outra combinação, como "nARutO" a máquina aceitará como válida a resposta.


        for i in range(len(array)):
        
            if (array [i] == captalize):
                achei = True

        if (achei == True):

            print("")
            print("Uhuuuul!")
            print("")
            print(f'Você digitou {captalize} que está na posição {array.index(captalize)} do nosso índice!')
            print("")
            print('Muito obrigado por participar. Abraços!')
            print("                                                                     Desenvolvido por Mauricio")

        # 3 - dados.index(nome) irá printar o número do índice que está o nome correto escolhido, lembrando que o índice começa do número 0.

        if (achei != True):
            print("Poxa vida! Eu ainda não tenho esse nome na minha base de dados.")
            print('Tente digitar outro.')

dados = ['Naruto', 'Sasuke', 'Orochimaru', 'Hokage', 'Sakura', 'Tsunade', 'Sasori', 'Gaara', 'Asuma', 'Kurenai', 'Zabuza', 'Haku', 'Kakashi', 'Ino', 'Chyoji', 'Jiraiya', 'Kabuto', 'Itachi', 'Raposa de 9 Caudas', 'Kankuro', 'Hinata', 'Akamaru']

personagens_naruto(dados)

#TESTE DE MERGE
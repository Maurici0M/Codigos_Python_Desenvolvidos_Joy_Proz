def idade_nascimento(ano_atual, ano_nascimento):
    res = ano_atual - ano_nascimento
    return res

ano_atual = 2022
ano = True

print("Digite o seu nome completo: ")
nome = str (input())
captalizado = nome.title() #Vai deixar todas as primeiras letras após o espaço, em maiúscula.

while ano == True:

  print("Digite o seu ano de nascimento: ")
  try: 

      ano_nascimento = int (input())
        
      if (ano_nascimento > 1923) and (ano_nascimento <= 2022):

          ano = False

          print("Dados validados com sucesso!")
          
          print(f'{captalizado} você tem {ano_atual - ano_nascimento} anos.')
          
          print("Fim")
          break

      else:
          print("Você digitou uma data de nascimento inválida.")
          print("Por favor, digite novamente o seu ano de nascimento.")
          
  except:
    print("Ocorreu um erro inesperado. Por favor, insira somente números na sua idade.")

idade_nascimento(ano_atual, ano_nascimento)
from logging import exception
def validar_numero ():
  numeroValido = False

  while(numeroValido == False):
    
    try:

      numero = int (input('Por favor, digite um número entre 0 e 100: '))

      if (numero > 100):

        print("Por favor, digite um número entre 0 e 100.")

      elif (numero < 0):
        print("Você precisa digitar um número positivo, entre 0 e 100.") 

      else:
        
        numeroValido == True

        print("Número validado com sucesso!")
        print("Você digitou o número: ", numero)
        break

    except:
      print("Você precisa digitar um número inteiro, entre 0 e 100")

validar_numero()
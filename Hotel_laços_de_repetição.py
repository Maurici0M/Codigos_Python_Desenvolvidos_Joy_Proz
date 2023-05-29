#Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13º andar.
#Escreva um código que imprima todos os números exceto o número 13.

# * * * Esse é o código com os comandos "for", "range", "continue e "break",que será executado de forma crescente (1,2,3...)

numero = 0


for i in range(0,21):


  numero = numero + 1


  if (numero == 13):
    continue


  if (numero == 21):
    break


  print("Subindo para o andar número: ",numero)
print('________________________________________')
 

  
#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)
# * * * Esse código lerá os andares de forma decrescente, pulando o andar de número 13, sem interromper a contagem.

numero = 0


for i in range(20,0,-1):


  numero = i -1


  if (numero == 13):
    continue


  if (numero == 20):
    break


  print("Descendo para o andar de número: ",numero)
print('________________________________________')

#Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.
# * * * Exemplo utilizando o comando "While" e "IF".


numeral = 1

while numeral <=20:
    if numeral != 13:
        print("Esse é o andar",numeral)
    numeral += 1
print('________________________________________')
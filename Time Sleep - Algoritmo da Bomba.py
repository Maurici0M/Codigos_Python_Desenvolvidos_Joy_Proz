import time

print('Iniciando contagem regressiva, utilizando "for, range e time.sleep"')
for i in range(30,0,-1):
    print(i)
    time.sleep(1)
else:
    print("BUUUUM!")

print("_____________________________________________")
print("")



print('Iniciando contagem regressiva, utilizando "while e i"')

i = 30

while i > -1:
    print(i)

    i = i - 1

else:
    print("Bum!")

print("_____________________________________________")
print("") #Pulará a próxima linha, para não ficarem unidas.



print('Iniciando a Contagem regressiva, utilizando "for"')
for i in range(30,0,-1):
    print(i)
    i = i - 1
else:
    print("BUUUUM!")


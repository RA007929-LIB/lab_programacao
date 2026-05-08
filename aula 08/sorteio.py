import random

x = int(input("digite um numero:"))
soma = 0
contador = 0

while contador <= x:
    numeroSorteado = random.randint(1,10)
    print (numeroSorteado)
    soma += numeroSorteado
    contador += 1

print (soma)
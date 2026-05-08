numero = int(input("digite um numero -> "))
numero2 = int(input("digite um numero -> "))

soma = 0
for i in range(numero, numero2 + 1):
    if(i%2 == 0):
        soma += i
print (soma)
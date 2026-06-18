lista1 = [1,2,6,5,4,8]
lista2 = [50,30,68,10]

listaNova = []
itensListaMaior = len(lista1)

if len(lista2) < itensListaMaior:
    lista_temp = lista1
    lista1 = lista2
    lista2 = lista_temp

iteracao = 0

while iteracao < itensListaMaior:
    if len(lista1) > iteracao:
        listaNova.append(lista1[iteracao])
    if len(lista2) > iteracao:
        listaNova.append(lista2[iteracao])
    
    iteracao += 1

print(lista1)
print(lista2)
print(listaNova)

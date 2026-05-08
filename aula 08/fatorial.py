numeroInicial = int(input('digite um numero pra vira fatoraial: -> '))
valorFatorial = numeroInicial

while numeroInicial > 1:
    valorFatorial *= numeroInicial - 1
    numeroInicial -= 1

print('fatoriao é ' + str(valorFatorial))
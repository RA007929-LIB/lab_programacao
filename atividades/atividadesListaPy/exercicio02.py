vetor = [20,30,58,65,78,89]
soma = 0

for i in vetor:
    soma += i
    media = soma / len(vetor)
print(f"A média é {media:.2f}")

parar = 1
possibilidade = 0

while parar == 1:
    for i in vetor:
        if(i <= media and i + possibilidade >= media) or (i >= media and i - possibilidade <= media):
            print(f"O numero mais próximo da média é {i}")
            parar += 1
            break
    possibilidade += 1
    
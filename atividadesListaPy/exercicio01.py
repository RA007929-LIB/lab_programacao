import random

jogadas = []
repeticoes = []


while len(jogadas) < 100:
    qtdJogada = random.randint(1,6)
    jogadas.append(qtdJogada)

repeticoes.append(jogadas.count(1))
repeticoes.append(jogadas.count(2))
repeticoes.append(jogadas.count(3))
repeticoes.append(jogadas.count(4))
repeticoes.append(jogadas.count(5))
repeticoes.append(jogadas.count(6))
    
print("-"*100)
print(f"JOGADAS DO DADO \n [1,2,3,4,5,6]\n \n{jogadas}")
print("-"*100)
print(repeticoes)
print("-"*100)



listaNotas = []
for notas in range(5):
    notasAlunos = float(input("Digite as notas dos alunos: "))
    listaNotas.append(notasAlunos)
listaNotas.remove(min(listaNotas))

print(listaNotas)
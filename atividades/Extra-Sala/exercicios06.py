lista = []

for i in range(5):
    nomes = input("Digite o nome desejado:")
    lista.append(nomes)

print(f"a lista é {lista}")

lista.reverse()

print(f"A lista inversa é {lista}")

lista = []
for i in range(1,7):
    num = int(input("Digite um número: "))
    lista.append(num)

print("="*123)

verificar = int(input("Digite um numero para verificação: "))

duplicadas = 0

for indice, i in enumerate(lista):
    if i == verificar:
        print(f"Foi verificado duplicado no índice {indice}")
        duplicadas += 1

print(f"Foi possivel verivicar {duplicadas} números iguais existentes na Lista")
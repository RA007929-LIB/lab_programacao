num = int(input("Digite o numero desejado > "))

impares = []
somaImpares = 1

for i in range(num):
    if i % 2 != 0:
        somaImpares *= i
        impares.append(i)
        if i >= num:
            break;
print(f"A multiplicação do intervalo de 0 a {num} é :{somaImpares}")
print("="*123)
print(f"Os numeros impares são :{impares}")

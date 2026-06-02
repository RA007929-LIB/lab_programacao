palavra = input("Digite uma palavra: ").lower()
contadorVogais = 0

for letra in palavra:
    if letra in ("aeiou"):
        contadorVogais += 1
print(f"A apalvra comtem {contadorVogais} vogais")

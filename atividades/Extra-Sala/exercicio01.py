while True:
    num = int(input("Digite o numero desejado (0 - para sair) > "))
    if num == 0:
        print("Você encerrou sua sessão!")
        break;

    if num >= 10 and num <= 50:
        print("Dado válido!")
    else:
        print("Dado inválido!")

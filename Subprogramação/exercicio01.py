def status(media):
        if media >= 7:
                return'Aprovado'
        elif media < 7 and media > 3:
                return 'Verificação Suplementar'
        elif media > 10:
                return 'Invalído'
        else:
                return 'Reprovado'
        
media = int(input('Digite a média do aluno > '))
print(status(media))
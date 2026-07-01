def celsius_para_fahrenheit(temperatura):
    fahrenheint = celsius * 1.8 + 32
    return fahrenheint

celsius = float(input(('Digite o valor em graus > ')))

print('-------Conversão de Temperaturaa-------')
print(f'Temperatura em Celsius {celsius}')
print(f'Temperatura em fahrenheint {celsius_para_fahrenheit(celsius)}')



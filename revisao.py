# print('REVISAO DE CARRO')
# print(30 * '-')
# Carro = input('Qual a marca do carro?')
# valor = float(input('Qual o valor do carro?'))
# km = input('Consumo km por litro?')
# print(30 * '-')
# print(f'| carro: {Carro}')
# print(f'| valor : R${valor}')
# print(f'| consumo por litro: {km}')
# print(30 * '-')


# print('CADASTRO')
# nome = input('| nome:')
# email = input('| email:')
# senha = input('| senha:')
# print()
# print('| Cadastro')
# print(f'| nome:{nome}')
# print(f'| email:{email}')
# print(f'| senha:{senha}')



# nome = input('Qual é seu nome?')
# idade = int(input('Qual a sua idade?'))
# if idade >= 18:
#     print('Maior de idade')
#     carteira = int(input('Posui carteira de motorista? (1 sim /2 nao)'))
#     if carteira == 1:
#         print('Pode dirigir')
#     else:
#         print('nao pode dirigir')

# else:
#     print('Menor de idade')


temperatura = int(input('Temperatura em graus celcius?'))
if temperatura >=30:
    print('esta quente')
elif temperatura >=20:
    print('esta agradavel')
elif temperatura >=10:
    print('esta frio')
elif temperatura >=0:
    print('Muito frio')
else:
    print('Muito,muito frio,congelando!!!')
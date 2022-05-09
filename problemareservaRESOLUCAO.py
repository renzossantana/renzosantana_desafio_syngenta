from datetime import datetime
from datetime import date
'''ENTRADA DE DADOS'''

tipo_do_cliente = str(input('Digite o seu tipo de assinatura: (Regular/Reward) '))
tempo_estadia = int(input('Por quantos dias deseja se hospedar?: '))

'''Variaveis'''
cont = 1
lakewood = 0
bridgewood = 0
ridgewood = 0
lista_lakewood = []
lista_bridgewood = []
lista_ridgewood = []

'''Laço para validação de datas'''
for cont in range(cont,tempo_estadia+1):
    print('Formado da data -=-=-=|DDMMMYYYY(AAAA)|=-=-=-')
    dataentrada = str(input('Digite a data a qual a data que deseja se hospedar: '))
    data_lista = list(dataentrada)

    if data_lista[9:] == ['(', 't', 'h', 'u', 'r', ')']:
            data_lista[9:] = ['(', 't', 'h', 'u', ')']
            dataentrada = "".join(data_lista)
    elif data_lista[9:] == ['(', 't', 'u', 'e', 's', ')']:
            data_lista[9:] = ['(', 't', 'u', 'e', ')']
            dataentrada = "".join(data_lista)

    data = datetime.strptime(dataentrada, '%d%b%Y(%a)')
    numero_dia_da_semana = data.isoweekday()


    if tipo_do_cliente == 'Regular':
        if numero_dia_da_semana > 5:
            lakewood = 90
            bridgewood = 60
            ridgewood = 150
        else:
            lakewood = 110
            bridgewood = 160
            ridgewood = 220
    if tipo_do_cliente == 'Reward' or tipo_do_cliente == 'Rewards':
        if numero_dia_da_semana > 5:
            lakewood = 80
            bridgewood = 50
            ridgewood = 40
        else:
            lakewood = 80
            bridgewood = 110
            ridgewood = 100

    lista_lakewood.insert(cont,lakewood)
    lista_bridgewood.insert(cont,bridgewood)
    lista_ridgewood.insert(cont, ridgewood)


soma_total_lakewood = sum(lista_lakewood)
soma_total_bridgewood = sum(lista_bridgewood)
soma_total_ridgewood = sum(lista_ridgewood)


if soma_total_lakewood < soma_total_bridgewood and soma_total_lakewood < soma_total_ridgewood:
    nome_do_hotel_mais_barato = 'Lakewood'

if soma_total_ridgewood < soma_total_bridgewood and soma_total_ridgewood < soma_total_lakewood:
    nome_do_hotel_mais_barato = 'Ridgewood'

elif soma_total_bridgewood < soma_total_ridgewood and soma_total_bridgewood < soma_total_lakewood:
    nome_do_hotel_mais_barato = 'Bridgwood'

elif soma_total_bridgewood == soma_total_ridgewood or soma_total_bridgewood == soma_total_lakewood or soma_total_ridgewood == soma_total_lakewood or soma_total_ridgewood == soma_total_bridgewood or soma_total_lakewood == soma_total_bridgewood or soma_total_lakewood == soma_total_ridgewood:
    nome_do_hotel_mais_barato = 'Ridgewood'

print(nome_do_hotel_mais_barato)








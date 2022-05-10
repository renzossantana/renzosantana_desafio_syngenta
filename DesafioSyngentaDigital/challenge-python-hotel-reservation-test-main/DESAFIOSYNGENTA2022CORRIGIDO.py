from datetime import datetime
import re
print('Digite a ENTRADA 1: ')
entrada = str(input())

#Divisão de caracteres (':' and ',')
entrada_formatada = (re.split(': |, ', entrada))

#Retirada de valores da STRING inteira para atribuição a outras variaveis
tipo_do_cliente = entrada_formatada[0]
data = entrada_formatada[1:]
maxrange = len(data) #range maximo for

#Declaração de variável
cont = 0
lakewood = 0
bridgewood = 0
ridgewood = 0
lista_lakewood = []
lista_bridgewood = []
lista_ridgewood = []



for cont in range(cont,maxrange):

    #Formatação para conversão de STR para tipo DATE
    data_lista = list(data[cont])
    if data_lista[9:] == ['(', 't', 'h', 'u', 'r', ')']:
        data_lista[9:] = ['(', 't', 'h', 'u', ')']
        data[cont] = "".join(data_lista)
    elif data_lista[9:] == ['(', 't', 'u', 'e', 's', ')']:
        data_lista[9:] = ['(', 't', 'u', 'e', ')']
        data[cont] = "".join(data_lista)

    #Conversão de STR -> DATE
    data_date = datetime.strptime(data[cont], '%d%b%Y(%a)')
    numero_dia_da_semana = data_date.isoweekday()

    #Chegagem do tipo do cliente
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

    lista_lakewood.insert(cont, lakewood)
    lista_bridgewood.insert(cont, bridgewood)
    lista_ridgewood.insert(cont, ridgewood)

soma_total_lakewood = sum(lista_lakewood)
soma_total_bridgewood = sum(lista_bridgewood)
soma_total_ridgewood = sum(lista_ridgewood)


#Escolha da opção mais barata

if soma_total_lakewood < soma_total_bridgewood and soma_total_lakewood < soma_total_ridgewood:
    nome_do_hotel_mais_barato = 'Lakewood'

if soma_total_ridgewood < soma_total_bridgewood and soma_total_ridgewood < soma_total_lakewood:
    nome_do_hotel_mais_barato = 'Ridgewood'

elif soma_total_bridgewood < soma_total_ridgewood and soma_total_bridgewood < soma_total_lakewood:
    nome_do_hotel_mais_barato = 'Bridgwood'

elif soma_total_bridgewood == soma_total_ridgewood or soma_total_bridgewood == soma_total_lakewood or soma_total_ridgewood == soma_total_lakewood or soma_total_ridgewood == soma_total_bridgewood or soma_total_lakewood == soma_total_bridgewood or soma_total_lakewood == soma_total_ridgewood:
    nome_do_hotel_mais_barato = 'Ridgewood'

print(nome_do_hotel_mais_barato)


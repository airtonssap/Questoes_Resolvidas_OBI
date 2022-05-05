#Total de peças a depender do tipo de jogo de dominó
total = 0

#Entrada
tipo_jogo_domino = int(input())

#Soma de peças por linha
for linha in range(1, tipo_jogo_domino+2):
    total += linha

#Saída
print(total)
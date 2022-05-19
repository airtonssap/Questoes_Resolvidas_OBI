#Entrada
n, x, y, z = [int(input()) for _ in range(4)]
evolucao = 0

#Desenvolvimento
lista = sorted([x,y,z])
for i in range(3):
    n -= lista[i]
    if n < 0:
        break
    else:
        evolucao += 1

#Saída
print(evolucao)
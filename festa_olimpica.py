#entrada
convidados = int(input('Quantidade de convidados: '))
c = list(range(1, convidados+1))

#corte
sorteios = int(input('Quantidade de sorteios para corte: '))
for i in range(sorteios):
    s = int(input('Número sorteado: '))
    del c[s-1::s]

#saída
soma = 0
for valor in c:
    print(valor)
    soma +=1
    if soma == 10000:
        break

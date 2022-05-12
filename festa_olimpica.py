#entrada
convidados = int(input('Quantidade de convidados: '))
c = list(range(1, convidados+1))

#corte
sorteios = int(input('Quantidade de sorteios para corte: '))
soma = 0
for i in range(sorteios):
    s = int(input('Número sorteado: '))
    for removidos in range(s, convidados+1, s):
        if removidos == s:
            soma = 0
        c.pop(removidos-1 - soma)
        soma += 1
    convidados -= soma

#saída
for valor in c:
    print(valor)
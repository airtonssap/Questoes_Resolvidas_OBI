#entrada
n, i, f = input().split()
lista = list()
for loop in range(int(n)-1):
    p,q,d = input().split()
    lista.append([int(p),int(q),int(d)])

atual = int(f)
valor1 = -1
valor2 = 0
valor3 = 0
soma = 0

#Excluindo as possibilidades que não satisfazem a questão
while True:
    for chave in range(len(lista)):
        if atual == lista[chave][0] and valor2 != valor1:
            soma += lista[chave][2]
            atual = lista[chave][1]
            if atual == int(i):
                break
            valor2 = valor1
            valor1 = lista[chave]
            valor3 = 0

        elif atual == lista[chave][1] and valor2 != valor1:
            soma += lista[chave][2]
            atual = lista[chave][0]
            if atual == int(i):
                break
            valor2 = valor1
            valor1 = lista[chave]
            valor3 = 0
    if atual == int(i):
        break
    valor3 += 1
    if valor3 >1:
        lista.remove(valor1)
        valor1 = -1
        valor2 = 0
        soma = 0
        atual = int(f)
#Saída
print(soma)
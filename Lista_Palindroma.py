
contador = 0
#Entrada do sistema
qntValores = int(input())
Valores = input().split()

#Verificação e contagem se a lista é palíndroma, isto é, nesse caso: L[i] = L[N-i], 
#onde L[i] representa o i-ésimo elemento da lista e N o último índice da lista.
if qntValores%2 == 0:
    for indice in range(0, int((qntValores)/2)):
        if Valores[indice] == Valores[qntValores-1-indice]:
            continue
        else:
            Valores[indice] += Valores[qntValores-1-indice]
            Valores[qntValores-1-indice] = Valores[indice]
            contador += 1

elif qntValores%2 != 0:
    for indice in range(0, int((qntValores+1)/2)):
        if Valores[indice] == Valores[qntValores-1-indice]:
            continue
        else:
            Valores[indice] += Valores[qntValores-1-indice]
            Valores[qntValores-1-indice] = Valores[indice]
            contador += 1
            
#Saída do sistema
print(contador)
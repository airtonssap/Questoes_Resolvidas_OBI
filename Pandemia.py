#Lista de infectados e quantidade de infectados
ListaInfectados = list()
Infectados = 0

#Entrada
Tamigos, Tdias = input().split()
Infectado, DiaInicioInfectado = input().split()

#Quantidade de pessoas na reunião no dia 'n' e as pessoas que estavam lá
for dia in range(1, int(Tdias)+1):
    Qnt_e_pessoas = input().split()
    
    #Inicio da contagem de infectados e lista de infectados
    if dia == int(DiaInicioInfectado):
        Infectados = int(Qnt_e_pessoas[0])
        for pessoa in range(1, len(Qnt_e_pessoas)):
            ListaInfectados.append(Qnt_e_pessoas.copy()[pessoa])
    
    #Comparação se nos outros dias as pessoas infectadas, através da lista de infectados,
    #estavam com pessoas não infectadas.
    elif dia > int(DiaInicioInfectado):
        for pessoa in range(1, len(Qnt_e_pessoas)):
            if Qnt_e_pessoas[pessoa] in ListaInfectados:
                for pessoa in range(1, len(Qnt_e_pessoas)):
                    if Qnt_e_pessoas[pessoa] not in ListaInfectados:
                        ListaInfectados.append(Qnt_e_pessoas.copy()[pessoa])
                        Infectados += 1
            continue
        continue

#Saída
print(Infectados)
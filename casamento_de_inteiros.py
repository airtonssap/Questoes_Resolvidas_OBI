v1 = input('Valor1: ')
v2 = input('Valor2: ')
r1 = ''
r2 = ''
if len(v1) > len(v2):
    while len(v1) > len(v2):
        v2 = '0' + v2
elif len(v1) < len(v2):
    while len(v1) < len(v2):
        v1 = '0' + v1

for i in range(len(v1)):
    if int(v1[i]) > int(v2[i]):
        r1 += v1[i]
    elif int(v1[i]) < int(v2[i]):
        r2 += v2[i]
    else:
        r1 += v1[i]
        r2 += v1[i]
if len(r1) == 0:
    r1 = '-1'
if len(r2) == 0:
    r2 = '-1'
print(f'{r2} {r1}')
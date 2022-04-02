'''dado uma matriz 3x3 imprima o somatorio dos elementos da diagonal secundaria
 1 1 1
 1 1 1
 1 1 1'''
 '''
matriz2 = []
matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = 0
for lin in range(3):
    for col in range(3):
        element = int(input('digite um elemento:'))
        matriz[lin][col] = element

   
print(matriz)


for lin in range(3):
    for col in range(3):
        if lin+col ==2:
        element = int(input('digite um elemento:'))
        matriz[lin][col] = element
        soma+= matriz[lin][col]
   
print(matriz)
'''
matriz = [[0,0,0], [0,0,0], [0,0,0]]
dimensao = 3
soma = 0

for lin in range(3):
    for col in range(3):
        element = int(input('digite um elemento:'))
        matriz[lin][col] = element



for lin in range(dimensao):
    for col in range(dimensao):
        if lin+col ==dimensao - 1:
            matriz[lin][col] = element
            soma+= matriz[lin][col]
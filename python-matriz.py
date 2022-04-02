matriz = [[0,0,0], [0,0,0], [0,0,0]]

#entrada de dados = input
for lin in range(3):
    for col in range(3):
        element = int(input('digite um elemento: mat [{lin}][{col}]:'))
        matriz[lin][col] = element

print(matriz)

#processamento = logica
soma = 0
dimensao = 3

for lin in range(dimensao):
    for col in range(dimensao):
        if lin + col == dimensao - 1:
            soma += matriz[lin][col]

#saida = output
print(soma)
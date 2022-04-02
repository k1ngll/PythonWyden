#o restaurante bembao cobra 12 reais por cada quilo de refeição,escreva um algoritmo que leia o peso do prato
# montado pelo clientes em quilos e imprima o valor a pagar. assuma que a balança ja desconte o peso do prato.
from re import X

precoquilo = 12
valor = 0
prato = float(input('digite o peso do seu prato em quilo:\n'))

valor = (precoquilo*prato)

print('o valor total a pagar é R$',valor)
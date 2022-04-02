#pesquisa salario e numeros de filhos

#a) media do salario da população
'''soma_salario = 0 
total_pessoas = 0
media_salario = soma_salario / total_pessoas
media_filhos = qtdfilhos / total_pessoas
maior_salario = primeiro_salario
total_pessoas_100/ total_pessoas'''

#input  
salario = float(input('informe o seu salario:'))
filhos = float(input('informe o numero de filhos:'))
total_pessoas = 0   
somatorio_salario = 0
qtdfilhos = 0
maior_salario = salario
salarios_100 = 0
salario = 0

while salario >= 0:
    

    total_pessoas +=1
    somatorio_salario += salario #somatorio de salario
    qtdfilhos += filhos #somatorio de filhos

    if maior_salario < salario:
        maior_salario = salario

    if salario < 100:
        salarios_100 +=1
    salario = float(input('informe o seu salario:'))
    filhos = float(input('informe o numero de filhos:'))


if total_pessoas >0:

    media_salario = somatorio_salario / total_pessoas
    media_filhos = qtdfilhos / total_pessoas
    salarios_100 = salarios_100 / total_pessoas

    
    print('media de salario da pop :' ,media_salario)
    print('media de filhos da pop',media_filhos)
    print('maior salario da pop',maior_salario)
    print('percentual de salario ate 100',salarios_100)
else:
    print('salario informado negativo')

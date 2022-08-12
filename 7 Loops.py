#Loop for

# Python
# for item in interavel:
#    execução do loop

# Utilizamos qualquer tipo de Loops para iterar sobre sequencias
                                        # ou valores iteiraveis
                                        #VALOR INTEIRAVEL EX:

                                        # nome = "maik"
                                        # nome
                                        # nome[0]
                                        # 'M'

# Exemplos Valores Iteraveis:
# - Strings (exemplo acima)
# - Listas
# [1, 3, 5, 7, 9]

# - Range
# numeros = range[1, 10]

'''
nome = 'Maik'
lista = [1, 3, 5, 7, 9]
numero = range(1, 10)    #temos que transformar em uma lista

# Exemplo 1 (Iterando sobre string)
for letra in nome:
    print(letra)


# Exemplo 2 (Iterando sobre Lista)
for numero in lista:
    print(numero)


# Exemplo 3 (Iterando sobre Range)
for numero in range(1, 10):
    print(numero)   # Range(valor_inicial até valor_final)
                    # Obs: o valor final o Range não inclui (ele pega o anterior)

'''

'''
nome = 'Maik'
lista = [1, 3, 5, 7, 9]
numero = range(1, 10)
'''

# enumerate:
# - (0, 'm') (1, 'a') (2, 'i') (3, 'k')
'''
for m, k in enumerate(nome):               # Entrega o nome pela quantidade
    print(nome)                            # de letras
'''

'''
for m, i in enumerate(nome):              #Entrega todas as letras
    print(nome[m])
'''

'''
for indice, letra in enumerate(nome):     #Entrega todas as letras
    print(letra)
'''

'''
for _, letra in enumerate(nome):      #Entrega todas as letras
    print(letra)                      #para descartar algum valor pode se usar o '_'
'''

'''
for valor in enumerate(nome):        # Entrega indice e valor
    print(valor)
'''

'''
for valor in enumerate(nome):
    print(valor[0])                  # Somento os indices
'''

'''
for valor in enumerate(nome):
    print(valor[1])                  # Somento as letras
'''

'''
qtd = int(input('Quantas vezes o loop deve rodar? '))  # Da a quantidade de numeros 
soma = 0                                               # Soma todos eles

for n in range(1, qtd + 1):
    print(f'imprimindo {n}')
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')
'''

'''
nome2 = 'maik lindo'           # Mostra o nome na mesma lingua
for letra in nome2:
    print(letra, end= '')
'''

'''
nome = 'maik'
nome * 2 = maikmaik
nome + ' lindo' = maik lindo

para colocar emojis no python voce pode acessar esse site:
https://apps.timwhitlock.info/emoji/tables/unicode
e pegar o unicode dos emojis

unicode original: U+1F30D
modificado: U0001F30D
Peguei a letra 'u', substitui o '+' por 000 e colei o restante

emoji = 'U0001F30D'

for x in range(3):                  # Quantidade de "triangulos de emojis"
    for num in range(1, 11):
        print('\U0001F30D' * num)   # coloca os emoji em "triangulo"
                                    #Tem que colcoar a '\' e os ''
                                    # A barra é pra ignorar algo
'''



'''
#Ranges (Utilizador para gerar Sequencias numericas especificas)
# Forma 1
for num in range(11):        # vai imprimir do 0 ao 10
    print(num)

# Forma 2
for num in range(1, 11):     # Nesse exemplo vai começar do 1 não do 0 pq foi especificado
    print(num)

# Forma 3
for num in range(5, 60, 5):   #Aqui ele vai do 5 ao 50 contando de 5 em 5
    print(num)

# Forma 4
for num in range(10, 0, -1):  # Do 10 ao 0 (Contagem regressiva! para ir até zero coloca '-1' no lugar do 0)
    print(num)

# No terminal:
# Para fazer uma list:   lista = list(range(10))   #lista 0 a 9
'''



'''
# While: vai repetir tudo enquanto o Boolean for verdadeiro

# EXEMPLO 1
numero = 1
while numero < 10:                 # Equanto numero for menor que 10
    print(numero)                  # Mostre numero
    numero = numero + 1            # Numero é igual a numero + 1

# Caso voce não colocar um criterio de parada o programa vai executar infinitamente

# EXEMPLO 2
resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou Jessica? ')
if resposta == 'sim':
    print('meme veio da porra')
'''



'''
# Break (Quebrar loops)
# EXEMPLO 1
for numero in range(1, 10):
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do loop!')

# EXEMPLO 2
while True:
    comando = input("Digite 'SAIR' para sair: ")
    if comando == 'sair':
        break
'''

while True:
    comando = input("Digite oque o mamalace é ")
    if comando == 'lindo':
        break
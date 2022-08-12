'''
Listas

As listas em python funcionam como arrays em C, porém diferentemente de arrays
podemos colocar diferentes tipos de dados e em python é mais dinamico

Dinamico:
- Não possui tamanho fixo, ou seja, podemos criar a lista do tamanho que quisermos
de acordo com nossa memoria do computador.
- Qualquer tipo de dado

As listas em Python são representadas em Python por []
'''

lista1 = [1, 99, 4, 27, 15, 22,3, 1, 44, 42,27]
lista2 = ['m', 'a', 'i','k', ' ', 'c', 'u', 's', 's', 'i', 'o', 'l', 'i']
lista3 = []
lista4 = list(range(11))
lista5 = list('Marcos Cussioli')
lista6 = [1, 2.1, True, 'maik', [40, 50, 60]]

'''
#   Podemos facilmente ver se um valor está contido na lista.
num = 5
if num in lista4:
    print(f'Tem aqui! {num}')
else:
    print(f'Tem nao {num}')
'''



'''
#   Podemos ordenar uma lista
lista1.sort()
print(lista1)
'''


'''
#   Podemos contar o numero de ocorrencias de um valor dentro da lista
print(f'Tem {lista1.count(1)} Numeros 1')
print(f"Tem {lista5.count('s')} letras s")
'''



'''
#   Adicionar Elementos em Listas: utilizar função append
#   com append conseguimos adicionar 1 elementro por ver apenas
print(lista1)
lista1.append(42)
print(lista1)

#   Da pra adicionar Listas dentro do Python
lista1.append([8, 3, 11])    # COLOCA COMO [SUBLISTA] NA LISTA
print(lista1)

if [8, 3, 11] in lista1:
    print('TA AQUI NA LISTA')
else:
    print('ta aqui não boy')

lista1.extend([123, 44, 67])    # ADICIONA SEU ELEMENTO NA LISTA
print(lista1)
'''



'''
#   Podemos inserir um novo elementro na lista, informando a posição do indice
#   Obs: Isso NÃO substitui o valor inicial, o mesmo é deslocado para a direita da lista
lista1.insert(2, 'novo valor')
print(lista1)

#   Juntar duas listas
lista1 = lista1 + lista2                 # lista1.expand(lista2) faz a mesma coisa
print(lista1)
'''



'''
lista1.reverse()             # Inverter a lista
print(lista1)
print(lista2[::-1])          # Inverter a lista
'''



'''
#   Copiar uma Lista
lista6 = lista2.copy()
print(lista6)
'''



'''
#   Qual o tamanho dessa lista?
print(f'tem {len(lista2)} algarismos nessa lista')
'''



'''
#   Remover O ULTIMO Elemento de uma lista
#   O .pop() Não somente remove o ultimo elemento, mas também retorna ele
print(lista5)
lista5.pop()
print(lista5)

#   Podemos remover um elemento pelo indice, ou seja pela posição
#   Os elementos a direita do indice são deslocados para ESQUERDA
#   Se não ouver elemento no indice informado, dará ERRO
lista5.pop(1)
print(lista5)
'''



'''
#   Limpar Completamente uma lista
lista5.clear()
print(lista5)
'''


'''
#   Repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)
'''



'''
#   Converter String em lista
#   Exemplo 1:                              # .split() Separa os elementos pelo espaço
curso = 'programação em Python essencial'
print(curso)
curso = curso.split()
print(curso)

#   Exemplo 2:                              # .split() Aqui falamos que o separador é a ,
curso1 = 'Programação,em,Python,essencial'
print(curso1)
curso1 = curso1.split(',')
print(curso1)

#   Exemplo 3:
curso1 = 'Programação, em, Python, essencial'
print(curso1)
curso1 = curso1.split(',')
print(curso1)
'''



'''
#   Colocando Espaço entre os caracteres
lista7 = 'Programação', 'em', 'Python', 'essencial'
curso = ' '.join(lista7)
print(curso)

curso = '/'.join(lista7)
print(curso)
'''



'''
#   Iterando sobre Listas
#   Exemplos 1: (For)

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

#   Exemplos 2: (For)
soma = ''
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)

#   Exemplos 3: (while) 
carrinho = []
produto = ''

while produto != 'sair':
    print("ADICIONE UM PRODUTO NA LISTA ou DIGITE 'sair' para sair")
    produto = input('Digite os produtos no carrinho: ')
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
'''



'''
#   Utilizando variaveis em Listas
numeros = [1, 2, 3, 4, 5]

num1 = 1
num2 = 2
num3 = 3           # OS DOIS METODOS SÃO A MESMA COISA
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

#   Looping "Cada cor vai printar ela
cores = ['verde', 'amarelo', 'azul', 'branco']
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
'''



'''
#   Em listas fazemos acesso aos elementos de forma indexada
#         0          1         2        3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[3])

#   Fazer os mesmos elementos ao contrario! (Com o negativo)
#   O fim de um elemento está ligado ao inicio da lista
print(cores[-3])
'''



'''
#   Gerar indice em um for
cores = ['verde', 'amarelo', 'azul', 'branco']
for indice, cor in enumerate(cores):           # Coloca chave na cor e numero na posição
    print(indice, cor)
'''



'''
#   listas aceita, valores repetidos
lista = []
lista.append(1)
lista.append(1)
lista.append(2)
lista.append(2)
lista.append(4)
lista.append(True)
print(lista)
'''



'''
#   Encontrar o indice de um elemento na lista
numeros = [5, 6, 7, 8, 9, 10]

#   Em qual indice está o valor 6?
print(numeros.index(9))
print(numeros.index(10, 4))           # Buscando o indice 10 apartir do indice 4
print(numeros.index(8, 6, 8))           # Buscando indice do valor 8, entre os indices 6 e 8
'''



'''
#   Revisão de slicing
#   Lista[inicio:fim:passo]
#   Range[inicio:fim:passo]

lista = [1, 2, 3, 4]
print(lista[1:])         # Iniciando no Indice 1 e pegando todos restantes
print(lista[:-2])        # Iniciando no Indice 0 e pega até o indice 2 - 1
print(lista[:4])         # Iniciando do 0 pega até o indice 4 - 1
print(lista[1:3])        # Iniciando do 1 pega até o indice 3 - 1

#   Trabalhando em slice de lista com o parametro "passo"
print(lista[1::2])       # Começa com 1, vai até o final, de 2 em 2
print(lista[::2])        # Começa em 0, vai até o final, de 2 em 2
'''



'''
#   Soma, Valor MAX, Valor MIN, Tamanho
#   Todos os valores devem ser inteiro ou reais

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(lista))  # SOMA
print(max(lista))  # MAX
print(min(lista)) # MIN
print(len(lista))  # TAMANHO
'''
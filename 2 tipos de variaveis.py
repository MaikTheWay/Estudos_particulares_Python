#Tipos de variaveis
#INT
# + = Plus
# - = Minus
# % = residue
# / = division (float)
# // = division (int)
# * = multiplication
# ** = elevated

print(1 + 1)
print(1 - 1)
print(4 % 2)        # or num 4 %= 2
print(4 / 2)        # or num 4 /= 2
print(1 * 2)        # or num 1 *= 2
print(8 ** 2)

num = 42
type(num)           # Para saber o tipo de numero
print(num + 1)

print(1_000_000)    # Voce pode separar as casas por . ou _



# FLOAT
# ERRADO -> ACABA GERANDO UMA TUPLA // NÃO PODE SEPARAR COM VIRGULA
valor, valor1 = 1, 44
print(valor)
print(valor1)

# CERTO
valor2 = 1.44
print(valor2)
print(type(valor2))

# Convertendo valores Float -> Int
resultado = int(valor2)
print(resultado)
print(type(resultado))

# NUMEROS COMPLEXOS
# coloca um "j" na frente do numero -> 5j

complexo = 5j
print(complexo)
print(type(complexo))



# BOOLEAN
verdadeiro = True
falso = False
print(verdadeiro)
print(falso)

# Negação (not)
# negação -> caso o valor boolean seja verdadeiro ele vai retornar falso
# o mesmo ocorre ao contrario
print(not verdadeiro)
print(not falso)

# Ou (or) -> ou um ou outro devem ser verdadeiros
# true or true      -> true
# true or false     -> true
# false or true     -> true
# false or false    -> false
# Vai priorizar o true(1)
print(verdadeiro or falso)

# E (and) -> ambos os valores devem ser verdadeiros
# true and true -> true
# true and false -> false
# false and true -> false
# false and false -> true

# 5 > 6 = False
# 6 > 5 = True
# 6 == 6 = true
# 4 <= 5 = true   (4 É MENOR OU IGUAL A 5?)

print(type(True))
print(type(False))



# STRING
# 'cu' -> string
# "cu" -> string
# '''cu''' -> string
# """cu""" -> string

nome = 'Maik Cussioli'
print(nome)
print(type(nome))

nome1 = 'maik \nlindo'
print(nome1)

nome1 = 'maik \flindo'
print(nome1)

estabelecimento = "gina's bar"  # Obrigatorio " " por causa do Gina's
print(estabelecimento)          # Da pra ser tbm Gina\'s bar

print(nome.upper())             # Todas as letras maiusculas
print(nome.lower())             # Todas as letras minusculas
print(nome.split())             # Coloca as palavras em uma lista de strings
print(nome[0:7])                # Vai da letra 0 até a 7 letra (conta os espaços)

print(nome.split()[0])
print(nome.split()[1])

print(nome[::-1])               # Comece do primeiro elemento e inverta ele com o
                                # ultimo  (inverte a string)

print(nome.replace('a', 'c'))   # Inverte uma letra por outra


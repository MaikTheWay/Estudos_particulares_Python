# OPERADORES UNARIOS: not
# OPERADORES BINARIOS: and, or, is

# PARA and AMBOS OS VALORES PRECISAM SER TRUE.
ativo = True               # SE MUDAR PARA False O USER NÃO VAI ESTAR LOGADO
logado = True

if ativo and logado:
    print('Bem vindo, User!')
else:
    print('Voce precisa ativar sua conta, por favor, cheque o email!')



# PARA or AMBOS OS VALORES PRECISAM SER TRUE.
ativo = False               # SE MUDAR PARA False O USER AINDA VAI ESTAR LOGADO
logado = True               # SE OS DOIS FOREM False NÃO VAI FUNCIONAR

if ativo or logado:
    print('Bem vindo, User!')
else:
    print('Voce precisa ativar sua conta, por favor, cheque o email!')



# PARA not O VALOR SEÁ BOOLEANO INVERTIDO (True Vira False) (False vira True)
ativo = True
logado = False

if not ativo:
    print('Voce precisa ativar sua conta, por favor, cheque o email!')
else:
    print('Bem vindo, User!')



# PARA is VAI COMPARAR UM VALOR COM OUTRO, E DIZER SE É TRUE OU FALSO

# 1 == 1             True
# maik == maik       True
# Maik == maik       False

ativo1 = True
# ativo é true?
print(ativo1 is True)
# o programa vai retornar "true" pq ele é true


ativo2 = False
# ativo é falso?
print(ativo1 is False)
# o programa vai retornar "false" pq ele é false

# para testar as funções boolean de True ou False
# terminal -> nome = 'maik' -> dir(nome) -> nome.islower()
# terminal -> nome = 'maik' -> dir(nome) -> nome.isupper()
# terminal -> nome = 'maik' -> dir(nome) -> nome.istittle()  (inicial do nome é maiuscula?)
# terminal -> nome = 'maik' -> dir(nome) -> nome.istittle().istittle()
                                            # (inicial do nome é maiuscula? e transforma a inicial em maiuscula)

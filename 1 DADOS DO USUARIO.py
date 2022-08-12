# RECEBENDO DADOS DO USUARIO
# Termianl > Python > Dir  para acessar recursos integrados a linguagem.
# CTRL + L -> Limpa o terminal

print('Olá qual seu nome?')
nome = input()

idade = int(input(f'Muito prazer {nome},qual sua idade ?'))
print(f'{nome} tem {idade} anos')


# Fazendo Cast -> todo dado recebido via input é tipo STRING
print(f'voce nasceu em {2022 - int(idade)}')



# 1
'''
num1 = input('Digite um numero: ')
num2 = input('Digite um numero: ')

if num1 > num2:
    print('O primeiro numero é maior')
else:
    print('O segundo numero9 é maior')
'''

# 2
'''
num1 = input('Digite um numero: ')

if int(num1) > 0:
    print(int(num1) **2)
else:
    print('Numero invalido!')
'''

# 3
'''
num1 = input('Digite um numero: ')

if int(num1) > 0:
    print(int(num1) **2)
else:
    print(int(num1) * int(num1))
'''

# 4
'''
num1 = input('Digite um numero: ')

if int(num1) > 0:
    print(int(num1) **2)
    print(int(num1) * int(num1))
'''

# 5
'''
num1 = input('Digite um numero: ')
if int(num1) % 2 == 0:
    print('Esse numero é par!')
else:
    print('É impar!')
'''

# 6
'''
num1 = input('Digite um numero: ')
num2 = input('Digite um numero: ')
difereca = int(num1) - int(num2)

if num1 > num2:
    print('O primeiro numero é maior')
else:
    print('O segundo numero é maior')
print(f'A diferença entre eles é de: {int(difereca)}')
'''

# 7
'''
num1 = input('Digite um numero: ')
num2 = input('Digite um numero: ')

if num1 == num2:
    print('Numeros iguais')
'''

# 8
'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

if nota1 > 0.0 and nota1 < 11.0:
    print('Notas validas')

elif nota2 > 0.0 and nota2 < 11.0:
    print('Notas validas')

else:
    print('NOTAS INVALIDAS')
'''

# 9  PERGUNTAR PARA O BERDA
'''
salario = float(input('SALARIO: '))
emprestimo = float(input('EMPRESTIMO: '))
prestacao = 0.2 * salario
conta = prestacao - salario

if prestacao > salario:
    print('Empréstimo Não concebido')

else:
    print('Empréstimo concebido')
'''

# 10
'''
homem = float(input('Digite a altura masculino: '))
mulher = float(input('Digite a altura feminina: '))

print(f'O Peso ideal MASCULINO É {(homem * 72.7) - 58}')
print(f'O Peso ideal FEMININO É {(mulher * 62.1) - 44.7}')
'''

#11
'''
x = int(input("Numero: "))
soma = 0

while (x != 0):
    resto = x % 10
    x = (x - resto)//10
    soma = soma + resto
print(soma)
'''

#12
'''
import math.pi

num = int(input('Digite um numero: '))
x = num.log(10)

if num < 0:
    print('Numero invalido')
else:
    print(x)
'''

#14
'''
trabalho = float(input('Nota do Trabalho: '))       #peso: 2
avaliacao = float(input('Nota da Avaliação: '))     #peso: 3
exame = float(input('Nota do Exame: '))             #peso: 5
media = float((trabalho + avaliacao + exame) / 3)

if media < 2.9:
    print(f'NOTA:{media} Está de REPROVADO')

if media < 4.9:
    print(f'NOTA:{media} Está de RECUPERAÇÃO')

else:
    print(f'NOTA:{media} Está APROVADO!')
'''

#16
'''
dia_da_semana = int(input('Qual dia é hoje: '))

if dia_da_semana == 1:
    print('Hoje é Domingo')

if dia_da_semana == 2:
    print('Hoje é Segunda')

if dia_da_semana == 3:
    print('Hoje é Terça')

if dia_da_semana == 4:
    print('Hoje é Quarta')

if dia_da_semana == 5:
    print('Hoje é Quinta')

if dia_da_semana == 6:
    print('Hoje é Sexta')

if dia_da_semana == 7:
    print('Hoje é Sabado')
'''


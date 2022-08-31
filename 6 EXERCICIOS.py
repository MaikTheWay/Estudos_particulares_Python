# Faça um programa que receba dois números e mostre qual deles é o maior.
num1 = input('Digite um numero: ')
num2 = input('Digite um numero: ')

if num1 > num2:
    print('O primeiro numero é maior')
else:
    print('O segundo numero9 é maior')



# Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
num1 = input('Digite um numero: ')

if int(num1) > 0:
    print(int(num1) **2)
else:
    print('Numero invalido!')



Leia um numero real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o numero ao quadrado.

num1 = input('Digite um numero: ')

if int(num1) > 0:
    print(int(num1) **2)
else:
    print(int(num1) * int(num1))



# Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
# O número digitado ao quadrado
# A raiz quadrada do número digitado

num1 = input('Digite um numero: ')
if int(num1) > 0:
    print(int(num1) **2)
    print(int(num1) * int(num1))



# Faça um programa que receba um número inteiro e verifique se este número é par ou Impar.
num1 = input('Digite um numero: ')
if int(num1) % 2 == 0:
    print('Esse numero é par!')
else:
    print('É impar!')



# Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.
num1 = input('Digite um numero: ')
num2 = input('Digite um numero: ')
difereca = int(num1) - int(num2)

if num1 > num2:
    print('O primeiro numero é maior')
else:
    print('O segundo numero é maior')
print(f'A diferença entre eles é de: {int(difereca)}')



# Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem Naseros iguais.
num1 = input('Digite um numero: ')
num2 = input('Digite um numero: ')

if num1 == num2:
    print('Numeros iguais')



# Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a media destas notas Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

if nota1 > 0.0 and nota1 < 11.0:
    print('Notas validas')

elif nota2 > 0.0 and nota2 < 11.0:
    print('Notas validas')

else:
    print('NOTAS INVALIDAS')



# Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso contrario imprima: Empréstimo concedido.
salario = float(input('SALARIO: '))
prestacao = float(input('PRESTAÇÃO: '))

if prestacao > salario * 0.2:
    print('Empréstimo Não concebido')

else:
    print('Empréstimo concebido')



# Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal
homem = float(input('Digite a altura masculino: '))
mulher = float(input('Digite a altura feminina: '))

print(f'O Peso ideal MASCULINO É {(homem * 72.7) - 58}')
print(f'O Peso ideal FEMININO É {(mulher * 62.1) - 44.7}')



# Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus algarismos.
numero = int(input('Digite um numero: '))
soma = 0
while numero > 0:
    soma += numero % 10
    numero = int(numero /10)
print(soma)



# Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número nválido". Se o número for positivo, calcular o logaritmo deste numero.
import math
num = int(input('Digite um numero: '))
x = int(num.log(10))

if num < 0:
    print('Numero invalido')
else:
    print(x)



# 13
nota1 = float(input('1º Nota: '))
nota2 = float(input('2º Nota: '))
nota3 = float(input('3º Nota: '))
media = (nota1 + nota2 + nota3) / 3

if media >= 60:
    print('Passou')
else:
    print('Não Passou')



# A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das très notas mencionadas anteriormente obedece aos pesos: Trabalho de Laboratório. 2: Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias.
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



# Escreva um programa que leia um inteiro entre 1 e 12 e impria o mês correspondente a este numero.
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



# Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que: A = ((Basemaior + Basemenor) * Altura) / 2
basemaior = float(input('Digite a base maior: '))
basemenor = float(input('Digite a base menor: '))
altura = float(input('Digite a altura: '))

if basemenor and basemaior and altura > 0:
    area = (basemaior + basemenor) * altura / 2
    print(area)



# Escreva um programa que aceite dois números e operadores matemáticos e execute a operação de acordo.
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
sinal = str(input('Digite a Operação desejada'))

if sinal == '+':
  print(num1 + num2)
if sinal == '-':
  print(num1 - num2)
if sinal == '**':
  print(num1 ** num2)
if sinal == '/':
  print(num1 / num2)
if sinal == '//':
  print(num1 // num2)
if sinal == '*':
  print(num1 * num2)
if sinal == '%':
  print(num1 % num2)



# Faça um programa para verificar se um numero inteiro é divisivel por 3 ou 5, mas não simultaneamente entre os dois
num = int(input('Digite um numero: '))
if num % 3 == 0 and num % 5 == 0:
    print(f'É DIVISILVEL POR 3 E 5: {num}')
else:
    if num % 3 == 0:
        print(f'É DIVISILVEL POR 3: {num}')
    if num % 5 == 0:
        print(f'É DIVISILVEL POR 5: {num}')



# Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo e, se forem, se é um triângulo escaleno, equilátero ou isóscele
plado = float(input('Digite o primeiro lado: '))
slado = float(input('Digite o segundo lado: '))
tlado = float(input('Digite o terceira lado: '))

if plado == slado == tlado:
    print('Triangulo EQUILÁTERO')
if plado == slado != tlado or plado == tlado != slado or tlado == slado != plado:
    print('Triangulo ISÓSCELES')
else:
    if plado != slado != tlado:
        print('Triangulo ESCALENO')



# Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida.
# Escolha a opção:
# 1- Soma de 2 números.
# 2- Diferença entre 2 números (maior pelo menor).
# 3- Produto entre 2 números.
# 4- Divisão entre 2 números (o denominador não pode ser zero).

from time import sleep
num1 = int(input('Primeiro numero: '))
num2 = int(input('Primeiro numero: '))
x = 0

while x != 5:
    print(f'[1] - SOMA\n[2] - DIFERENÇA\n[3] - PRODUTO\n[4] - DIVISÃO\n[5] - BYE BYE')
    x = int(input('Qual função voce quer? '))
    if x == 1:
        print(num1 + num2)
    elif x == 2:
        if num1 > num2:
            print(num1 - num2)
        else:
            print(num2 - num1)
    elif x == 3:
        if num1 or num2 < 0:
            print(num1 * num2)
    elif x == 4:
        print(num1 / num2)
    elif x == 5:
        print('Finalizando....')
        sleep(5)
    print('\n')
print('Acabou o programa! Vlw Flw!')


# Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições para aposentadoria são:
# Ter pelo menos 65 anos,
# Ou ter trabalhado pelo menos 30 anos,
#Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input('Qual sua idade: '))
trabalho = int(input('Quantos anos voce ja trabalhou: '))
if idade >= 65 or trabalho >= 30 or idade >= 60 and trabalho >= 25:
    print('pode aposentar')
else:
    print('Não pode')



# Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for divisivel por 400 ou se for divisivel por 4 e não for divisivel por 100. Por exemplo: 1988, 1992, 1996
ano = int(input('Digite o ano: '))
if ano % 400 == 0 or ano % 4 == 0:
    print('Ano bissexto')
elif ano % 100 == 0:
    print('Não é bissexto')
else:
    print('Não é bissexto')



# Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado. possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Faça um programa em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagern de erro
print('1- MG\n2- SP\n3- RJ\n4- MS')
estado = int(input('Insira o NUMERO do Estado que voce deseja enviar o produto: '))
valor = int(input('Valor do Produto: '))

if estado == 1:
    print(f'VALOR DO IMPOSTO: {valor * 0.07}')
if estado == 2:
    print(f'VALOR DO IMPOSTO: {valor * 0.12}')
if estado == 3:
    print(f'VALOR DO IMPOSTO: {valor * 0.15}')
if estado == 4:
    print(f'VALOR DO IMPOSTO: {valor * 0.08}')
else:
    print('Digite um valor valido para o estado!')



# Calcule as raizes da equação de 2° Grau
import math
a = float(input('Digite o a: '))

if a <= 0:
    print("O 'a' não pode ser 0, não é uma equação do segundo grau!")
else:
    b = float(input('Digite o b: '))
    c = float(input('Digite o c: '))
    delta = ((b * b) - (4 * a * c))
    if delta < 0:
        print('"A equação não possui raízes reais.')
    elif delta == 0:
        raiz = -b / (2*a)
        print(raiz)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'1º Raiz: {raiz1}')
        print(f'2º Raiz: {raiz2}')



# em um percurso, calcule o consumo em Km/l escreva uma mensagem de acordo com a tabela abaixo:
# menor que 8 = Venda o carro!
# entre 8 e 14 = Económico!
# maior que 12 = Super economico!
km = float(input('Digite a distancia em Km: '))
l = float(input('Quantidade de gasolina em litros consumida pelo carro: '))
valor = km/l

if valor < 8:
    print('VENDA O CARRO!')
elif valor >= 8 and valor <= 14:
    print('Economico!')
elif valor > 12:
    print('SUPER ECONOMICO')



# Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
# Infantil A = 5 a 7
# Infantil B = 8 a 10
# Juvenil A = 11 a 13
# Juvenil B = 14 a 17
# Senior = maiores de 18 anos

idade = int(input('Digite a idade do nadador: '))

if idade >= 5 and idade <= 7:
    print('INFANTIL A')
elif idade >= 8 and idade <= 10:
    print('INFANTIL B')
elif idade >= 11 and idade <= 13:
    print('JUVENIL A')
elif idade >= 14 and idade <= 17:
    print('JUVENIL B')
else:
    print('SENIOR')



# Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das seguintes médias de acordo com um valor numérico digitado pelo usuário:
# Geométrica
# Ponderada
# Harmonica
# Aritmética

import numpy as np
x = float(input('X: '))
y = float(input('Y: '))
z = float(input('Z: '))

geometrica = x * y * z
print(f'geometrica: {np.cbrt(geometrica)}')

ponderada = (x + 2 * y + 3 * z) / 6
print(f'ponderada: {ponderada}')

harmonica = 1 / ((1/x) + (1/y) + (1/z))
print(f'harmonica: {harmonica}')

aritmetica = (x + y + z) / 3
print(f'aritmética: {aritmetica}')

# EXERCICIOS

# Faça um programa que leia um número inteiro e o imprima.
num = 1
print(num)



# Peça ao usuário para digitar três valores inteiros e imprima a soma deles. 4. Leia um número real e imprima o resultado do quadrado desse número.
valor1 = input('digite um numero: ')
valor2 = input('digite um numero: ')
valor3 = input('digite um numero: ')
soma = int(valor1) + int(valor2) + int(valor3)
print(soma)



# Leia um número real e imprima a quinta parte deste número.
num = input('digite um numero: ')
raiz = float(num) ** 2
print(f'A raiz de {num} é {raiz}\n')



# Leia um número real e imprima a quinta parte desse numero.
num = input('digite um numero: ')
dividir = int(num) / 5
print(dividir)



# Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é: FC (9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit e Ca temperatura em Celsius.
celsius = input('Digite a temperatura em Celsius: ')
fahrenheit = float(celsius) * (9.0 / 5.0) + 32.0
print(f'A temperatura em fahrenheit é {fahrenheit}')



#  Leia uma temperatura em graus Fahrenheit e apr sente-a convertida em graus Celsius. A fórmula de conversão é: C=5.0 (F-32.0)/9., sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
fahrenheit = input('Digite a temperatura em fahrenheit: ')
celsius = 5.0 * (float(fahrenheit) - 32.0) /9.0
print(f'A temperatura em celsius é {celsius}')



# Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A fórmula de conversão é: CK-273.15, sendo Ca temperatura em Celsius e Ka temperatura em Kelvin.
kelvin = input('Digite a temperatura em Kelvin: ')
celsius = float(kelvin) - 273.15
print(celsius)



# Leia uma temperatura em graus Celsius e apresente a convertida em graus Kelvin. A fórmula de conversão é: KC 273.15, sendo Ca temperatura em Celsius e Ka temperatura em Kelvin.
celsius = input('Digite a temperatura em  Celsius: ')
kelvin = float(celsius) + 273.15
print(kelvin)



# Leia uma velocidade em km/h (quilómetros por hora) e apresente-a convertida em m/s (metros por segundo). A fórmula de conversão é: MK/3.6, sendo K a velocidade em km/h e 1/ em m/s.
km = input('Qual a velocidade do veiculo em KM/H ?')
ms = float(km) / 3.6
print(ms)



# Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilômetros por hora). A fórmula de conversão é: K = M * 3.6 , sendo K a velocidade em km/h e M em m/s.
ms = float(input('Digite a velocidade em M/S: '))
km = ms * 3.6
print(km)



#  Leia uma distância em milhas e apresente a convertida em quilómetros. A fórmula de conversão é K = 1,61 * M
milha = float(input('Digite a distancia em MILHAS: '))
km = 1.61 * milha
print(km)



# Leia uma distância em quilómetros e apresente a convertida em milhas. A fórmula de conversão é M = K/2.57 sendo a distância em quilómetros e M em milhas.
km = float(input('Digite a distancia em KILOMETROS: '))
milhas = km/1.61
print(milhas)



# Leia um ángulo em radianos e apresente-o convertido em graus. A fórmula de conversão dot e / G = R * 180 / pi sendo Go ângulo em graus e R em radianos e = 3.14 16.
radiano = input('Apresente um Angulo Radiano: ')
graus = float(radiano) * 180/3.14
print(graus)



# Leia um valor de massa em quilogramas e apresente-o convertido em fibras. A formula de conversão é L = K/0.45 sendo K a massa em quilogramas e L a massa em libras.
quilogramas = input('Qual a massa em quilogramas: ')
libras = float(quilogramas) / 0.45
print(libras)



# Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores
value1 = input('insira um valor: ')
value2 = input('insira um valor: ')
value3 = input('insira um valor: ')
print(float(value1) **2 + float(value2) **2 + float(value3) **2)



# Leia quatro notas, calcule a média aritmética e imprima o resultado
value1 = input('insira a primeira nota: ')
value2 = input('insira a segunda nota: ')
value3 = input('insira a terceira nota: ')
value4 = input('insira a quarta nota: ')
print((int(value1) + int(value2) + int(value3) + int(value4)) / 6)



# Leia um valor em real e a cotação do dolar. Em seguida, imprima o valor correspondente em dólares
real = input('insira a nota: ')
cotação = float(real) * 5.35
print(cotação)



# Leia um numero inteiro e imprima o seu antecessor e o seu sucessor
numero = input('Digite um numero:')
antecessor = int(numero) - 1
sucessor =  int(numero) + 1
print(f'{antecessor}\n{numero}\n{sucessor}\n')



# Sejam A e B catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = a² + b² ao quadrados, Faça um programa que recebe A e B e imprima o valor da formula
catetoa = input('cateto a:')
catetob = input('cateto b:')
hipotenusa = ((float(catetoa) **2) + (float(catetob))) / 2
print(float(hipotenusa))



# Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%
product = input('what is the value of this product?')
discont = 12/100 * float(product)
print(float(product) - float(discont))



# Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de das trabalhados pelo encanador e imprima a quantia liquida que deverá ser paga, sabendo se que são descontadon 81% para imposto de renda.
dias = input('Digite o numero de dias trabalhados: ')
pagar = float(dias) * 30.00
desconto = (8/100 * float(pagar))
print(float(pagar) - float(desconto))



# Faça um programa para converter uma letra maiúscula em letra minúscula.
nome = input('Digite uma palavra com letras maiusculas: ')
print(nome.lower())



#  Faça um programa que leia um número inteiro positivo de très digitos (de 100 a 999)
num = input('Digite um numero com 3 Digitos: ')
print(num[::-1])



# Leia um número inteira de 4 digitos (de 1000 a 9999) e imprima 1 digito por linha.
num = input('Digite um numero maior que 4 digitos: ')
a = str(num)
print(f'{format(a[3])}')
print(f'{format(a[2])}')
print(f'{format(a[1])}')
print(f'{format(a[0])}')



# Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido pro porcionalmente ao valor que cada deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.
apostador1 = float(input('Quantia do primeiro apostador:'))
apostador2 = float(input('Quantia do segundo apostador:'))
apostador3 = float(input('Quantia do terceiro apostador:'))
premio = float(input('Valor do premio:'))

conta = premio / (apostador1 + apostador2 + apostador3)

print(f'Quantia do primeiro apostador: {apostador1 * conta}')
print(f'Quantia do segundo apostador: {apostador2 * conta}')
print(f'Quantia do terceiro apostador: {apostador3 * conta}')



# Faça um programa para ler as dimensões de um terreno (comprimento e e largura 7), bem como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno com tela.
largura = input('tamanho da largura: ')
comprimento = input('tamanho do comprimento: ')
conta = (float(comprimento) * float(largura))
tela = float(conta) * 75.00
print(f'O terreno tem {conta} em metros quadrados e o preço para colocar tela nele é de {tela}')




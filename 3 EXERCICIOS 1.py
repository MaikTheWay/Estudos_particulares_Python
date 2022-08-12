# EXERCICIOS
'''
#1 e #2
num = 1
print(num)
'''


'''
#3
valor1 = input('digite um numero: ')
valor2 = input('digite um numero: ')
valor3 = input('digite um numero: ')
soma = int(valor1) + int(valor2) + int(valor3)
print(soma)
'''

'''
#4
num = input('digite um numero: ')
raiz = float(num) ** 2
print(f'A raiz de {num} é {raiz}\n')
'''

'''
#5
num = input('digite um numero: ')
dividir = int(num) / 5
print(dividir)
'''

#6
'''
celsius = input('Digite a temperatura em Celsius: ')
fahrenheit = float(celsius) * (9.0 / 5.0) + 32.0
print(f'A temperatura em fahrenheit é {fahrenheit}')
'''

'''
#7
fahrenheit = input('Digite a temperatura em fahrenheit: ')
celsius = 5.0 * (float(fahrenheit) - 32.0) /9.0
print(f'A temperatura em celsius é {celsius}')
'''

'''
#8
kelvin = input('Digite a temperatura em Kelvin: ')
celsius = float(kelvin) - 273.15
print(celsius)
'''

'''
#9
celsius = input('Digite a temperatura em  Celsius: ')
kelvin = float(celsius) + 273.15
print(kelvin)
'''

'''
#10
km = input('Qual a velocidade do veiculo em KM/H ?')
ms = float(km) / 3.6
print(ms)
'''

#  ///// os proximos serão apenas 2 por pag do pdf, para evitar repetição ////

# Segunda página

'''
#15
radiano = input('Apresente um Angulo Radiano: ')
graus = float(radiano) * 180/3.14
print(graus)
'''

'''
#20
quilogramas = input('Qual a massa em quilogramas: ')
libras = float(quilogramas) / 0.45
print(libras)
'''

# Terceira página

'''
#28
value1 = input('insira um valor: ')
value2 = input('insira um valor: ')
value3 = input('insira um valor: ')
print(float(value1) **2 + float(value2) **2 + float(value3) **2)
'''

'''
#29
value1 = input('insira a primeira nota: ')
value2 = input('insira a segunda nota: ')
value3 = input('insira a terceira nota: ')
value4 = input('insira a quarta nota: ')
print((int(value1) + int(value2) + int(value3) + int(value4)) / 6)
'''

'''
#30
real = input('insira a nota: ')
cotação = float(real) * 5.35
print(cotação)
'''

# Quarta página

'''
#31
numero = input('Digite um numero:')
antecessor = int(numero) - 1
sucessor =  int(numero) + 1
print(f'{antecessor}\n{numero}\n{sucessor}\n')
'''

'''
#35
catetoa = input('cateto a:')
catetob = input('cateto b:')
hipotenusa = ((float(catetoa) **2) + (float(catetob))) / 2
print(float(hipotenusa))
'''

#37
'''
product = input('what is the value of this product?')
discont = 12/100 * float(product)
print(float(product) - float(discont))
'''

'''
#40
dias = input('Digite o numero de dias trabalhados: ')
pagar = float(dias) * 30.00
desconto = (8/100 * float(pagar))
print(float(pagar) - float(desconto))
'''

# Quinta página

'''
#45
nome = input('Digite uma palavra com letras maiusculas: ')
print(nome.lower()) 
'''

'''
#46
num = input('Digite um numero com 3 Digitos: ')
print(num[::-1])
'''

#52

apostador1 = input('Quantia do primeiro apostador:')
apostador2 = input('Quantia do segundo apostador:')
apostador3 = input('Quantia do terceiro apostador:')
premio = input('Valor do premio:')

conta = float(premio) - float(apostador1)
conta2 = float(premio) - float(apostador2)
conta3 = float(premio) - float(apostador3)

print(f'primeiro ganhador: {conta} ')
print(f'segundo ganhador: {conta2}')
print(f'terceiro ganhador: {conta3}')

'''
#53
largura = input('tamanho da largura: ')
comprimento = input('tamanho do comprimento: ')
conta = (float(comprimento) * float(largura))
tela = float(conta) * 75.00
print(f'O terreno tem {conta} em metros quadrados e o preço para colocar tela nele é de {tela}')
'''

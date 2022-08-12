#1
'''                                            O numero é divisivel por 3?
num = int(input('Digite um numero: '))

if num % 3 == 0:
    print('Numero é divisivel por 3!')
else:
    print('Esse numero NÃO é')
'''



#2
'''                                             Conte até 100                                 
for num in range(0, 101):
    print(num)
    
contador = 0
while contador < 101:
    print(contador)
    contador = contador + 1
'''



#3
'''                                             Conte até 10 e FIM
for num in range(1, 11):
    print(num)
    if num == 10:
        print('FIM!')
'''


#4
'''                                             Conte até 100_000 
x = 0
while x < 100_001:
    print(x)
    x = x + 1000
'''



#5
'''                                          Quantidade de numeros e some todos
qtd = int(input('Digite um numero: '))
soma = 0

for n in range(1, qtd + 1):
    print(f'imprimindo {n}')
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')
'''

#6 e #7
'''
total = 0                                   Faz uma media de 10 numeros POSITIVOS
for _ in range(10):
    n = int(input('Digite 10 numeros: '))
    if n < 0:
        pass
    total += n / 3
print(total)
'''


#8
'''                                         Faz uma media de 10 numeros POSITIVOS
maior = menor = 0
total = 0
for _ in range(10):
    n = int(input('Digite 10 numeros: '))
    if total == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'Maior valor: {maior} ')
print(f'Menor valor: {menor} ')
'''



#9
'''                                      Verifica se o numero é par ou impar
for _ in range(2):
    num = int(input('Digite 2 Numeros: '))
    if num % 2 == 0:
        print('Par')
    else:
        print('Impar')
'''



#10
'''
qtd = 51
for num in range(0, qtd, 2):
    print(num + num)
'''



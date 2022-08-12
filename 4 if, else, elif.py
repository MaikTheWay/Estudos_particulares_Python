idade = input('digite sua idade: ')

if int(idade) < 18:
    print('Menor de idade')

elif int(idade) == 18:
    print('Tem exatamente 18')

elif int(idade) == 25:
    print('Tem exatamente 25')

else:
    print('Maior de idade')

#if (se)
#else (se não)
#elif (junção dos dois acima e pode ter mais de um elif)
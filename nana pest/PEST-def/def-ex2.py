def positivo(num : float):
        if num > 0:
             return True
        else:
             return False

n = float(input('numero: '))

if positivo(n) == True:
    print('é positivo')

else:
    print('não é positivo')



#outra forma
def positivo(num : float):
        if num > 0:
             return 'positivo'
        else:
             return 'negativo'

n = float(input('numero: '))

if positivo(n) == 'positivo':
    print('é positivo')

else:
    print('não é positivo')


# 2° forma
    
def positivo(num : float):
        if num > 0:
             return 'positivo'
        else:
             return 'negativo'

n = float(input('numero: '))

x = positivo(n)

print('o número', n, 'é: ',x)

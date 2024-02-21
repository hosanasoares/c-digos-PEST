a = int(input('digite o primeiro número:'))
b = int(input('digite o segundo número:'))
c = int(input('digite o terceiro número:'))
n = int(input('digite o quarto número:'))

conv = (a**n)+(b**n)
conv1 = c ** n

if  conv == conv1:
    print('está de acorto com o teorema de fermat')
else:
    print('não está de acordo')
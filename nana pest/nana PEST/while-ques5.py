num = int(input('digite um numero inteiro:'))

cont = 0 

while num != 0:
    inver = num % 10
    cont = cont * 10 + inver
    num = num // 10

print(cont)
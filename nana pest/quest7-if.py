num = int(input('digite um número inteiro:'))

uni = num % 10
cent = num // 100 
dez = num - cent - uni

conv = (uni * 100) + (dez * 10)+ cent

if num == conv:
    print('é palindromo')


else:
    print('não é palindromo')
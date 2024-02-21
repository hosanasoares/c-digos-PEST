num1 = int(input('digite o primeiro número:'))
num2 = int(input('digite o segundo número:'))
num3 = int(input('digite o terceiro número:'))


if num1 == num2 or num2==num3 or num3==num1:
    print('por haver dois números iguais, a soma será igual a zero.')

else:
    soma = num1 + num2 + num3
    print(soma)
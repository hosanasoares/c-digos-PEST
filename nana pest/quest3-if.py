num = int(input('digite um número inteiro:'))

if num > 10 and num < 20:
    print(f'o número {num} é maior que 10 e menor que 30.')

elif num > 30 or num < 5:
    print(f'o número {num} é maior que 30 ou menor que 5.')

else:
    print(f'o número {num} não é maior que 10 e menor que 20 e não é maior que 30 ou menor que 5.')

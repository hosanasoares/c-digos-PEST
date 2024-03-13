def contar_digitos(num : int):
    uni = num % 10

    cont = uni + 1
    num = num// 10
    
    return cont

num = int(input('digite um número inteiro:'))

while num < 0:
    num = int(input('digite um número inteiro:'))


res = contar_digitos(num)
print(res)
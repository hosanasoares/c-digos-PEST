num = int(input('digite um número inteiro:'))

origi = num
quat = len(str(num))
sum = 0


while num > 0:
    vari = num % 10
    sum =sum + vari ** quat
    num = num // 10


if sum == origi:
    print(f'o número {origi} é Amstrong') 

else:
     print(f'o número {origi} não é Amstrong') 
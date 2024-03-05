num = int(input('digite um número: '))

count = 0

for n in range(1,num+1):
    if num % n == 0:
        count+= 1

if count == 2:
    print('é primo.')

else:
    print('não é primo.')
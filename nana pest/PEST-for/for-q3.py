num = int(input('digite um número: '))

count = 0

for h in range(0,num+1,2):
        count+=h
print('a soma dos números pares de 0 á', num,'é:', count)
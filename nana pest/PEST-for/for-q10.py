num = int(input('digite um número: '))
count = 0
for n in range(num,0,-1):

    if n % 3 == 0 or n % 5 == 0:
        count += n

print(count)

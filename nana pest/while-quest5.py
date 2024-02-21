num = int(input('digite um número inteiro'))

inver = 0
while True:
    uni= num % 10
    inver *= 10 + uni
    print(inver)
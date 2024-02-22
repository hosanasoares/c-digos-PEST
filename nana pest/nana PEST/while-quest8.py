num = 10011

cont = 0
exp = 0

while num > 0:

    dec = num % 10

    if dec == 0 or dec == 1:
        cont = cont + dec * (2**exp)
        exp += 1
        num //= 10

    else:
        print('não é binário') 

print(f'o número em decimal é:{cont}')

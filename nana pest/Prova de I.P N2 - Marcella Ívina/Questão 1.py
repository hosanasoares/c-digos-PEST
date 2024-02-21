# Sequência de Fibonacci
n = int(input('Quantos termos você quer que apareça ?  '))
t1 = 0 
t2 = 1
print(f'{t1} --> {t2} ', end='')
contador = 0
while contador <= n:
    t3 = t1 + t2
    print(f'--> {t3} ', end='')
    contador += 1
    t1 = t2
    t2 = t3


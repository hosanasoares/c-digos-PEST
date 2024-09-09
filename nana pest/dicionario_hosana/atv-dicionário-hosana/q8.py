votos =  [1, 2, 3, 1, 2, 1, 3, 3, 1, 2]
dic = {}

valor1 = 0
valor2 = 0 
valor3 = 0 

for n in votos:
    if n == 1:
        valor1 += 1

    elif n == 2:
        valor2 += 1

    elif n == 3:
        valor3 += 1

for i in range(1,4):
    if i == 1:      
        dic[i] = valor1

    elif i == 2:
        dic[i] = valor2

    elif i == 3:
        dic[i] = valor3

print(dic)
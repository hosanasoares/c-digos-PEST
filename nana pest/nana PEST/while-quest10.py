inicio = int(input('digite o início do intervalo:'))
fim = int(input('digite o fim do intervalo:'))


num = inicio

while num < fim:
    soma = 0
    quat = len(str(num))
    origi = num
    while origi > 0:
        vari = origi % 10
        soma =soma + vari ** quat
        origi = (origi - origi % 10) // 10
   

    if num == soma:
        print(num)
    
    num += 1

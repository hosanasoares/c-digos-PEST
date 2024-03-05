inicio = int(input('diga o numero para o inicio do intervalo: '))
fim = int(input('diga o numero para o fim do intervalo: '))

for n in range(inicio,fim+1):

    soma = 0 
    quant = len(str(n))
    ori = n

    while ori > 0:
        uni = ori % 10
        soma += uni ** quant
        ori = ori // 10

    if soma == n:
      print(soma)




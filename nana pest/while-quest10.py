fim = int(input('digite um número inteiro: '))


count = 1
 

while count < fim:
    soma = 0
    quat = len(str(count))
    origi = count
    while count >= 1:
        vari = count % 10
        soma =soma + vari ** quat
        count = (count - count % 10) // 10
   

    if soma == origi:
        print(origi)
    
    count+= 1

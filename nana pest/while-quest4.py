while True:
    num = int(input('digite um número inteiro:'))

    cont = 1

 
    if num == 0:
        break

    while cont <=num :
       if num % cont == 0:
            print(cont)
       cont+=1
        


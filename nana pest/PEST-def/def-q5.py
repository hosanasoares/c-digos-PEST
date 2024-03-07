def regressiva(n1 : int, n2 : int, pas : int):
    
    if n1 < n2:
        for i in range(n1, n2+1,pas):
         print(i)
        

    elif n1 > n2:
        pas *= -1
        for i in range(n1,n2-1,pas):
           print(i)



n1 = int(input('digite o inicio do intervalo: '))
n2 = int(input('digite o fim do intervalo: '))
pas = int(input('digite os passos em que a contagem ocorrerá: '))

regressiva(n1,n2,pas)

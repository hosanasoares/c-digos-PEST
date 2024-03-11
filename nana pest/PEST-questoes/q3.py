def eh_par(num : int):

    if num % 2 == 0:
        return True
    
    else:
        return False
    


while True:
    num = int(input('digite um número para saber se é par ou ímpar ou digite 0 para sair: '))
    if num == 0:
        break
    res = eh_par(num)
    print(res)
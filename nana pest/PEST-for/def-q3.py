def contador(inicio : int, fim : int, passo : int):
    if fim < inicio:
         passo *=-1
         for a in range(inicio,fim-1,passo):
             print(a)
    elif inicio < fim:
      for n in range(inicio,fim+1,passo):
            print(n)


ini = int(input('digite o inicio da contagem:'))
fim = int(input('digite o fim do intervalo:'))
pa = int(input('digite os passos que a contagem realizará:'))

contador(ini,fim,pa)
def positivo(num : float):
     if num > 0:
         return True
     return False

def negativo(num : float):
     if num < 0:
         return True
     return False

  
def zero(num : float):
     if num == 0:
         return True
     return False



#função sem retorno
def verifica(num : float):
    if positivo(num):
        print('positivo')

    elif negativo(num):
        print('negativo')

    elif zero(num):
        print('numero zero')


while True:
    n = float(input('digite um número: '))
    verifica(n)
from random import randint


def jogo_adivinhacao(num : int):
     

     aleatorio = randint(1,100)
     count = 0
     
     while num <= 0:
      num = int(input('[ERROR 404] -> valor inválido. adivinhe um número de 1 a 100: '))
      count +=1

     while num > 100:
      num = int(input('[ERROR 404] -> valor inválido. adivinhe um número de 1 a 100: '))
     

     while num < aleatorio:
       num = int(input('número muito baixo. digite outro valor:'))
       count +=1
     while num > aleatorio:
         num = int(input('número muito alto. digite outro valor:'))
         count +=1


     if num == aleatorio:
      print('Parabéns, você acertou!!!!! com ', count, 'tentativas')


num = int(input('ADIVINHE O NÚMERO !!!! -> digite um número de 1 a 100: '))
jogo_adivinhacao(num)




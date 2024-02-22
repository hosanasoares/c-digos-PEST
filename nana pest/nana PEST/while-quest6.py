import random

num = random.randint(1,9)

entr = int(input('adivinhe um número entre 1 e 9:'))

while entr !=0:
    if entr < num : 
        entr = int(input('muito baixo. Adivinhe outro número entre 1 e 9:'))

    elif entr > num:
        entr = int(input('muito alto. Adivinhe um número entre 1 e 9:'))

    else:
        print('você acertou!!!')
        break

    #perg = str(input('deseja sair? [sim]ou[não]:')).lower()


    #if perg == 'sim' or 's':
      #      continue

    #else:
     #    print('você foi um ótimo jogador. Volte mais vezes!')        
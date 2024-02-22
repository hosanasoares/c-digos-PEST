num = ('um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quartoze','quinze','desseseis','desessete','dezoito','dezenove','vinte')

uni = int(input('digite um número entre 1 e 20:'))

while uni < 1 or uni > 20:
    uni = int(input('valor errado. digite um número entre 1 e 20:'))

if uni <= 20 and uni >=1:
    uni -=1
    print('você digitou o número ',num[uni])
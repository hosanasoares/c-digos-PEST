# Calculando médias e exindo resultado 

print('-' *90)
print('''Olá professor(a), sou um calculador de médias automático.
Você irá colocar a notas do seu aluno quantas vezes desejar.
Para sair do programa e obter o resultado você irá digitar: 0 ''')
print('-' *90)

contador = 0
acumulador = 0

while True:
    nota = float (input('Insira a nota: '))
    acumulador += nota
    contador += 1
    if nota == 0:
        break
contador -= 1 
media = acumulador / contador  
print('-'*90)
print(f'Você colocou {contador} notas e sua média é {media} ')
print('-'*90)
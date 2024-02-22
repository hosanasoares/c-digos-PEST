
#tuplas

lanche = ('suco','pizza','laranja','feijão','ostra')

#posição do lanche
print(lanche[-2])

for comida in lanche:
    print('eu vou comer',comida)

for quant in range (0,len(lanche)):
    print(lanche[quant])

for quant1 in range(0, len(lanche)):
    print(f'eu vou comer:{lanche[quant]} ')

for quant2 in range (0, len(lanche)):
    print(f'eu vou comer  {lanche [quant2]} na posição  {quant2} da minha lista')

for pos, comida in enumerate(lanche):
    print(f'irei comer {comida} na posição {pos}')

print(sorted(lanche))

# juntar duas tuplas

a = (1,2,3,4,2,5)
b =(96,97,98,99,100)
c = a + b

print(c.index(5))
print(c.index(2, 1))

# deletar a tupla

pessoa = ('aline',12,'F',38.99)
del(pessoa)



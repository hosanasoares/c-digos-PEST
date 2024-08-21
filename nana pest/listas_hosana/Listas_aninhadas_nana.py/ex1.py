L = ['c', 4, [1,2,3,4], 'uva', ' ']

print(len(L))
print(L[2][0])
print(L[2][1])
print(L[2][2])
print(L[2][3])
#print(L[2][4]) erro, pois não existe


m = [[3,4],
     [5,6],
     [7,8]] #três elementos

#crie uma lista e mostre os elementos dela.

for n in m:
    for i in n:
        print(i)

for i in range(3):
    for j in range(2):
        print(m[i][j])
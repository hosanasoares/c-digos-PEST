num = 100
soma = 0

for i in range(1,num+1):
    count = 0
    for k in range(1,i+1):
        if i % k == 0:
         count+=1

    if count == 2:
        soma += i

print(soma)
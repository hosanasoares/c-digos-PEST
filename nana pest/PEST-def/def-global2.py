def funcao1():
    x= 10
    print(x) #10
    funcao2()
    print(x) #10

def funcao2():
    global x
    x = 20 
    print(x) #20



x = 0
print(x) #0
funcao1()#10, 20, 10
print(x)#20
funcao2()#20
print(x)#20
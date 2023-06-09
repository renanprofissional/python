def fibonacci (x):
    '''if x != 1:
        x = 1
    y = x + x
    y = x + y
    
    x = 1 + 1
    y = 2 + 1
    y = 3 + 2
    y = 5 + 3
    novo = atual + anterior
    novo = y + x
    z = y + x
    z = (x+x)'''
    print(x)
    if x < 100:
        fibonacci (x+(x+x/2))
        
print(fibonacci(1))
# 1, 1, 2, 3, 5, 8, 13, 21,...
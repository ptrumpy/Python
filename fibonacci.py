def fibo():
    n = 0
    n2 = 1
    num = int(input('How many times would you like the fibonacci sequence to run? '))

    fiboSum = 0
    for i in range(1,num + 1):
        n = n2
        n2 = fiboSum
        fiboSum = n + n2
    print(fiboSum)
fibo()    

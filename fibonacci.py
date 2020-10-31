# produces the nth fibonacci number
def fibonacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

# writes the first n fibonacci numbers
def fib(n):
    A=[]
    for i in range(1,n+1):
        A.append(fibonacci(i))
    return A

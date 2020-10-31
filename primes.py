def prime(n):
    if (n<2)or(int(n)!=n):
        return False
    for i in range(2,1+int(n**0.5)):
        if n%i==0:
            return False
    return True
def primes(m,n):
    A=[]
    for i in range(m,n+1):
        if prime(i):
            A.append(i)
    return A

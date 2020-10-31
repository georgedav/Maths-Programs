def divisors(n):
    A=[1,n]
    for i in range(2,1+int(n**0.5)):
        if n%i==0:
            A.append(i)
            if n/i !=i:
                A.append(int(n/i))
    A.sort()
    return A

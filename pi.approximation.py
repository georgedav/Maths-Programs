# approximates pi by using a random number generator, using the geometry and equation
# of a circle
import random
def pi_approx(n=100000):
    count=0
    for i in range(n):
        x=random.random()
        y=random.random()
        r=(x**2)+(y**2)
        if r<=1:
            count+=1
    return (4*count/n)

import math
from turtle import*
def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return  12*math.cos(k)-5*\
            math.cos(2*k)-2*\
            math.cos(3*k)-\
            math.cos(4*k)
speed(10000000)
bgcolor("black")
for i in range(6000):
    goto(hearta(i)*5,heartb(i)*5)
    for i in range(5):
        color("#f73487")
    goto(0,0)
    
done()


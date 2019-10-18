#******************************************************************************
# yield.py
#******************************************************************************
# Name: Simon Mei
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):none
#
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
import math
c1=float(input('Coupon 1: '))
c2=float(input('Coupon 2: '))
c3=float(input('Coupon 3: '))

b=float(input('Bond price: '))

t1=float(input('Time 1: '))
t2=float(input('Time 2: '))
t3=float(input('Time 3: '))

x=0.1

def f(x):
    return c1*math.exp(-x*t1) + c2*math.exp(-x*t2) + c3*math.exp(-x*t3) - b
    
    
def fp(x):
    return -t1*c1*math.exp(-x*t1) - t2*c2*math.exp(-x*t2) - t3*c3*math.exp(-x*t3)

for i in range(1,101):
    x = x - f(x)/fp(x)
    
print(x)

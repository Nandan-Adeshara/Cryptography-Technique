# Finding GCD of 2 num
''' 1 condition for Extended Euclidian Algorithm is the gcd should be 1 or numerator 
    and denominator should be coprime.
    So if num and denom are coprime another implication will be that it will be 
    automatically multiplicative inverse which will be helpful in finding the 
    solution.'''

import os

def gcd(num=None,denom=None): 

    if num == None or denom == None: # no None entry should be accepted
        return "Please provide Numerator and Denominator"
    elif denom == 0:
        return "Cannot Divide with 0 Denominator"
    elif num == 0:
        return 0
    elif num%denom==0:
        return denom
    else:
        result = num % denom
        num = denom
        denom = result
        return gcd(num,denom)

def extendedGCD(gcd):

    if gcd != 1:
        a = "Extended GCD is not possible as numerator and denominator are not coprime."
        return a
    else:
        return "EXtended GCD Possible"


os.system('cls')
n,d = input("Enter Numerator :"),input("Enter Denominator :")
print "GCD of {} and {}: {}".format(n,d,gcd(n,d))

# nx + dy = gcd(n,d)
print extendedGCD(gcd(n,d))
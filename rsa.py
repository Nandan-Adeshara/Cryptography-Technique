''' RSA-Rivest Samir Adleman is an asymmetric cryptography which
    uses stream cipher.
'''
from os import system 
import random

def prime(check = None):
    
    num = random.randint(1,100) if check== None else check

    prime_stat = True
    for i in range(2,num): # prime num can have 2 factors ' 1 and num itself'
        if num%i==0:
            prime_stat = False
            # mul1 = i
            # mul2 = num/i
            break

    # if prime_stat == False:
    #     print "{} is not prime because |{} X {} = {}|".format(num,mul1,mul2,num)
    # else:
    #     print "{} is prime num".format(num)

    if prime_stat == True:
        return num # returns prime
    
    return prime() # makes sure to return a prime


def rsa(pT = 1): # takes 1 as default plain text

    n = prime()
    g = prime()
    # if n or g becomes 1 then prod_mo will become 0 which makes denominator 0
    if n==1:
        n = prime()
    if g==1:
        g = prime()
    
    prod = n*g # product of generated primes
    
    prod_mo = (n-1)*(g-1) # product of minus one
    # generating public key E. Condition is 1<E<prod_mo and gcd(E,prod_mo)

    E = [] # public key list
    
    for i in range(2,prod_mo):
        if (prod_mo%i)!=0 and i==prime(i):
            E.append(i) # OR E = i and break

    E = 2 if len(E) == 0 else min(E)

    D = [] # private key list
    for i in range(2,10000):
        if (i*E)%prod_mo==1:
            D.append(i) # or D = i and break

    D = min(D)
    
    cT = pow(pT,E) % prod
    re_pT = pow(cT,D) % prod

    return cT,re_pT

system('cls')
pT = input("Enter Num:")
rsa = rsa(pT)
print "Plain Text <--> {} || Cipher Text <--> {}".format(rsa[1],rsa[0])

'''
Note - 
1. Because of some large prod_no calc the public key gets empty
'''
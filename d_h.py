# DH Key exchange
''' DH is an asymmetric key exchange encryption which takes a public and private keys to exchange data '''
import random,os

def DH(r1,r2): # taking 2 random nums as parameter
    ''' r1 and r2 are actually private keys to sender and reciever respectively'''

    p1 = prime()   # prime 1 is generally smaller
    p2 = prime() # prime 2 is generally bigger for security purpose
    #print p1,p2
    send = pow(p2,r1) % p1 # sender sends his public key to reciever 

    recv = pow(p2,r2) % p1 # reciever sends his public key to sender

    k1 = pow(recv,r1) % p1 # reciever will share his public key to sender
    k2 = pow(send,r2) % p1 # sender will share his public key to reciever

    return k1,k2

def prime(check = None):
    
    num = random.randint(1,100) if check== None else check

    prime_stat = True
    for i in range(2,num): # prime num can have 2 factors ' 1 and num itself'
        if num%i==0:
            prime_stat = False # turns the flag False
            break

    if prime_stat == True:
        return num # returns prime
    
    return prime() # makes sure to return a prime

print prime()

os.system('cls')
r1 = input("Select any random number For A: ")
r2 = input("Select any random number For B: ")

dh = DH(r1,r2)
print "Key for them is {} and {},which should be same.".format(dh[0],dh[1])
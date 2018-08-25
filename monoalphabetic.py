# Code to implement Monoalphabetic Cryptography

'''
Monoalphabetic is a substitution Encryption algorithm which substitutes itself 
with the next word in the Plaintext by uppercase of next letter . 
'''

import string,os

az = string.ascii_lowercase[:26]
AZ = string.ascii_uppercase[:26]

def monoalphabetic(pT = ""): # takes a plainText 

    cipherText = ""

    for i in pT: #iterates each letter of the pT

        if i == " ":
            cipherText += i
        elif i in az:
            i = az.index(i)
            if i==25: # if index goes out of range
                i = -1  
            cipherText += AZ[i+1]
        elif i in AZ:
            i = AZ.index(i)
            if i == 25: # if index goes out of range
                i = -1
            cipherText += az[i+1]
        else: # For unsupported characters (error handling)
            return None

    return cipherText

def decrypt_Monoalphabetic(cT = ""):

    plainText = ""
    if cT == None: # if the cT is None it will not iterate futher
        return None

    for i in cT:
        if i == " ":
            plainText += i
        elif i in az:
            i = az.index(i)
            if i == 0: # if index goes out of range
                i = 26
            plainText += AZ[i-1]
        elif i in AZ:
            i = AZ.index(i)
            if i == 0: # if index goes out of range
                i = 26
            plainText += az[i-1]
        else:
            return None

    return plainText

os.system('cls')
while True: # Continuos loop
    msg = raw_input("Enter a PlainText : ")

    print "\nMonoalphabetic Encryption-\n|<{}> --> <{}>  |".format(msg,monoalphabetic(msg))
    print "\nDecryption of Monoalphabetic Algorithm-\n|<{}> --> <{}>  |".format(monoalphabetic(msg),decrypt_Monoalphabetic(monoalphabetic(msg)))
    opt = raw_input("Interesting...Y/N? :").lower()
    if opt == "y":
        os.system('cls')
    else:
        break

'''Some Points to Note-
1. With errors wrong key could be generated which will be giving wrong encrypted and decrypted outputs.
2. Scope of this technique is limited as only single substituition of letter takes place.

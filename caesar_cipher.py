#a_z = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
import string,os

az = string.ascii_lowercase[:26] # writes small a_z
AZ = string.ascii_uppercase[:26]

def caesarCipher(inp="",shift = 11): # takes default input as None and shift as 11

    cipherText = "" # takes the ciphered string
    
    for i in inp:
        if i in az:
            ind = az.index(i)
        elif i in AZ:
            ind = AZ.index(i)

        shifts = ind + shift # performs the value of shifts
        
        if shifts >=26:
            shifts = shifts - 26 # reduces the shifts if greater than 25
            
        if i==chr(32): # counts space as it is
            cipherText+=i
        elif i>=chr(65) and i<=chr(122): # for upper and lower cases char cipher
            if i >= chr(65) and i <= chr(90):
                i = AZ[shifts]
                cipherText += i
            elif i>=chr(97) and i<=chr(122):
                i = az[shifts]
                cipherText +=i
        else: # for the rest of chars apart from lower,upper and space
            en = ord(i) + shift # performs the value of shifts
            cc = chr(en) # caesar cipher 
            cipherText+=cc
    
    return cipherText

def decrypt_caesarCipher(cipher,shift = 11): # takes default decryption shift as 1
    decrypt = "" # stores the decrypted message

    for i in cipher:
        if i in az:
            ind = az.index(i)
        elif i in AZ:
            ind = AZ.index(i)

        oli = ind - shift
        if oli<0:
            oli = oli + 26

        if i==chr(32):
            decrypt+=i
        elif i>=chr(65) and i<=chr(122):
            if i >= chr(65) and i <=chr(90):
                decrypt += AZ[oli]
            elif i>=chr(97) and i <= chr(122):
                decrypt += az[oli]
        else:
            msg = ord(i) - shift  # shift takes negative shifts to match the string
            pt = chr(msg) # plain text
            decrypt+=pt

    return decrypt

while True:
    os.system("cls")
    msg = raw_input("Enter Your Message : ")
    print "Caesar Ciphered Text -\n|<{}> ---> <{}> |".format(msg,caesarCipher(msg))
    print "\nDecrypted Caesar-\n|<{}> --> <{}>  |".format(caesarCipher(msg),decrypt_caesarCipher(caesarCipher(msg)))
    opt = raw_input(".\n.\nInteresting...Y/N:").lower()
    if opt == "y":
        pass
    else:
        break
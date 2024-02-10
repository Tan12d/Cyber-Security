import random
import math

prime = set()

def prime_filler():
    prime_check=[True]*250
    prime_check[0]=False
    prime_check[1]=False
    
    for i in range(2,256):
        for j in range(i*2,250,i):
            prime_check[j]=False
            
    for i in range(len(prime_check)):
        if prime_check[i]:
            prime.add(i)
            
    #print(prime)
    

def randomprime():
    rand = random.randint(0,len(prime)-1)
    
    it = iter(prime)
    
    for _ in range(rand):
        next(it)
        
    res= next(it)
    prime.remove(res)
    
    return res
    
def set_primes():
    p=randomprime()
    q=randomprime()
    
    # print(p)
    # print(q)
    
    global n
    n= p*q
    
    phi = (p-1)*(q-1)
    
    global e
    e=2
    
    while True:
        if math.gcd(e,phi)==1:
            break
        e+=1
    
    global d
    d=0
    
    while True:
        if (d*e)%phi==1:
            break
        d+=1
        
    # print(e)
    # print(d)
    
    
def encrypt(val):
    encry_text= pow(val,e)%n
    
    return encry_text
    
def encoder(message):
    enc=[]
    
    for char in message:
        enc.append(encrypt(ord(char)))
        
    return enc
    
def decrypt(val_1):
    decry=pow(val_1,d)%n
    return chr(decry)
    
def decoder(code):
    s=""
    for i in range(len(code)):
        s+=decrypt(code[i])
        
    return s

if __name__=="__main__":
    prime_filler()
    set_primes()
    
    message = input('Enter the plain text in small letters only: ')

    print("\nPlain Text: ")
    print(message)
    
    code = encoder(message)

    print("\nEncoded message: ")
    print(''.join(str(p) for p in code))

    print("\nDecoded message: ")
    print(''.join(str(p) for p in decoder(code)))
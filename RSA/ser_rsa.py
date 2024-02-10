import socket
import math
import random
from string import ascii_letters
s=socket.socket()
s.bind(('localhost',9999))
s.listen(1)
print('Server listening...')

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

while True:
    conn,addr = s.accept()
    msg=conn.recv(1024).decode()
    print('Received plain_text:',msg)

    prime_filler()
    set_primes()

    code = encoder(msg)
    conn.send(bytes(str(code),'UTF-8'))
    
    d_bytes = d.to_bytes(4, byteorder='big')  # 4 bytes for a 32-bit integer
    n_bytes = n.to_bytes(4, byteorder='big')

    conn.send(d_bytes)
    conn.send(n_bytes)


    conn.close()
    break


s.close()
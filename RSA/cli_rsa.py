import socket
from string import ascii_letters
cipher_letters='nzghqkcdmyfoialxevtswrupjbNZGHQKCDMYFOIALXEVTSWRUPJB'
c=socket.socket()
c.connect(('localhost',9999))
print('Client connected')
pt=input('Enter plain text:')
c.send(bytes(pt,'UTF-8'))

def decrypt(val_1):
    decry=pow(val_1,d)%n
    return chr(decry)
    
def decoder(code):
    s=""
    for i in code:
        s+=decrypt(int(i))
        
    return s

while True:
    received_cipher=c.recv(1024).decode()
    received_d_bytes = c.recv(4)  
    received_n_bytes = c.recv(4)

    # Convert bytes to integers
    d = int.from_bytes(received_d_bytes, byteorder='big')
    n = int.from_bytes(received_n_bytes, byteorder='big')

    # print(f'd = {d}')
    # print(f'n = {n}')
    
    new_received_cipher = received_cipher.replace(",","").replace(" ","").replace("[","").replace("]","")
    print('\nReceived cipher: ')
    print(new_received_cipher)

    val = list(received_cipher.replace("[","").replace("]","").replace(" ","").split(","))

    print("\nDecoded message: ")
    print(''.join(str(p) for p in decoder(val)))

    break


c.close()
import socket
from string import ascii_letters
cipher_letters='nzghqkcdmyfoialxevtswrupjbNZGHQKCDMYFOIALXEVTSWRUPJB'
c=socket.socket()
c.connect(('172.17.37.95',9999))
print('Client connected')
pt=input('Enter plain text:')
c.send(bytes(pt,'UTF-8'))

while True:
    received_cipher=c.recv(1024).decode()
    print('Received cipher:',received_cipher)
    trans=str.maketrans(cipher_letters,ascii_letters)
    print('Decrypted text:',received_cipher.translate(trans))
    break
c.close()
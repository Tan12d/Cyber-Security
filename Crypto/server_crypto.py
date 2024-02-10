import socket
from string import ascii_letters
s=socket.socket()
s.bind(('localhost',9999))
s.listen(1)
print('Server listening...')

while True:
    conn,addr = s.accept()
    msg=conn.recv(1024).decode()
    print('Received plain_text:',msg)
    cipher_letters='nzghqkcdmyfoialxevtswrupjbNZGHQKCDMYFOIALXEVTSWRUPJB'
    trans=str.maketrans(ascii_letters,cipher_letters)
    ciphered=msg.translate(trans)
    conn.send(bytes(ciphered,'UTF-8'))
    conn.close()
    break
s.close()
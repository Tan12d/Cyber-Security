import threading
import socket
client= socket.socket()
alias=input('Choose an alias >>>')
#client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
client.connect((host,9999))
def client_receive():
    while True:
        try:
            message=client.recv(1024).decode('utf-8')
            if message=="alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break

def client_send():
    while True:
        message=f'{alias}:{input("")}'
        client.send(message.encode('utf-8'))

receive_thread=threading.Thread(target=client_receive)
receive_thread.start()
send_thread=threading.Thread(target=client_send)
send_thread.start()
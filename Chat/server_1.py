import socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
LOCALHOST='127.0.0.1'
port=9990

server_socket.bind((LOCALHOST,port))
server_socket.listen(5)

print("Server started...")

conn,addr=server_socket.accept()

while True:
    msg_received=conn.recv(1024)
    msg_received=msg_received.decode()
    print("Client:",msg_received)

    msg_send=input("Me:")
    conn.send(msg_send.encode("ascii"))


    
server_socket.close()
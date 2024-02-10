import socket

def receive_file(server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', server_port))
    server_socket.listen(1)

    print(f"Server listening on port {server_port}...")

    connection, address = server_socket.accept()
    print(f"Connection from {address}")

    with open('received_file.txt', 'wb') as file:
        data = connection.recv(1024)
        while data:
            file.write(data)
            data = connection.recv(1024)

    print("File received successfully.")
    connection.close()
    server_socket.close()

if __name__ == "__main__":
    server_port = 12345
    receive_file(server_port)

import socket

def send_file(server_ip, server_port):
    file_path = input("Enter the path of the file you want to send: ")

    try:
        with open(file_path, 'rb') as file:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((server_ip, server_port))

            data = file.read(1024)
            while data:
                client_socket.send(data)
                data = file.read(1024)

            print("File sent successfully.")
            client_socket.close()

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if __name__ == "__main__":
    server_ip = '127.0.0.1'
    server_port = 12345

    send_file(server_ip, server_port)

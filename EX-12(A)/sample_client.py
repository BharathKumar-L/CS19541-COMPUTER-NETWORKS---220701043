import socket
 
def tcp_client(host='127.0.0.1',port=12345):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host,port))
        print("Connected to the chat server.")
        while True:
            message=input("CLient: ")
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            if data.decode().lower()=="bye":
                print("Connection closed by the server.")
                break
            print(f"Server: {data.decode()}")

tcp_client()

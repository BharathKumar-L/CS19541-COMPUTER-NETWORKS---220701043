import socket

def tcp_server(host='127.0.0.1',port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host,port))
        server_socket.listen()
        print(f"TCP server is listening to {host}:{port}")
        while True:
            conn,addr= server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if data.decode().lower()=="bye":
                        print("Client disconnected")
                        break
                    print(f"Client:{data.decode()}")
                    message = input("Server: ")
                    conn.sendall(message.encode())

tcp_server()


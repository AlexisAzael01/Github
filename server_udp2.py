import socket

IP = "192.168.1.70"  
PORT = 12345  

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((IP, PORT))

print(f"Servidor UDP  en {IP}:{PORT}...")

while True:
    data, addr = server_socket.recvfrom(1024)  
    print(f"Mensaje recibido de {addr}: {data.decode()}")

    response = "Mensaje recibido"
    server_socket.sendto(response.encode(), addr)


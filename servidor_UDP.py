import socket

# Dirección IP y puerto en los que el servidor estará escuchando
IP = "0.0.0.0"  # Escucha en todas las interfaces de red
PORT = 80     # Puerto del servidor UDP

# Crear socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Asociar el socket con la dirección IP y el puerto
server_socket.bind((IP, PORT))

print(f"Servidor UDP  en {IP}:{PORT}...")


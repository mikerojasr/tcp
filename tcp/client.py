import socket

HOST = '127.0.0.1'  # Dirección del servidor (localhost)
PORT = 5000         # Puerto del servidor

# Crear socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("Se establece una conexión con el servidor.")

while True:
    # Pedir mensaje al usuario
    message = input("Ingresa mensaje (o 'DESCONEXION' para salir): ")

    # Enviar mensaje al servidor
    client_socket.sendall(message.encode('utf-8'))

    # Cerrar conexión si el usuario ingresa "DESCONEXION"
    if message == "DESCONEXION":
        print("Cerrando conexión con el servidor...")
        break

    # Recibir y mostrar respuesta del servidor
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Respuesta del servidor: {response}")

client_socket.close()
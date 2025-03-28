import socket

# Configuración del servidor
HOST = '127.0.0.1' # Dirección IP local
PORT = 5000        # Puerto de escucha

# Crear el socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()  # El servidor está listo para aceptar conexiones

print(f"Servidor TCP en esperando conexiones en {HOST}:{PORT}")

while True:
    # Aceptar conexión de un cliente
    client_socket, client_address = server_socket.accept()
    print(f"Conexión establecida con el cliente {client_address}")

    while True:
        # Recibir mensaje del cliente
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break  # En caso de que no haya datos

        print(f"Mensaje recibido: {data}")

        if data == "DESCONEXION":
            print(f"El cliente {client_address} solicita desconexión.")
            client_socket.close()  # Cerrar conexión con el cliente actual
            break
        else:
            # Responder al cliente con el mensaje en mayúsculas
            response = data.upper()
            client_socket.sendall(response.encode('utf-8'))
            print(f"Respuesta enviada al cliente: {response}")
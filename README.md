# TCP Servidor y Cliente en Python
Este proyecto implementa un servidor y cliente por medio del protocolo TCP con sockets, desarrollado en el lenguaje Python.
El servidor permite la recepción de mensajes por el puerto 5000 de un cliente que establece la conexión y contesta el mensaje de vuelta en mayusculas, así mismo si recibe la palabra DESCONEXION, cierra la conexión con el cliente que envía este mensaje y se mantiene activo para nuevas conexiones.

## Autor
- Michael Rojas Rodríguez

## Requisitos
- Python 3.x instalado.
- Archivos `server.py` y `client.py` en el mismo directorio.

## Cómo ejecutar
1. **Ejecutar el Servidor TCP**  
   Abre una terminal y navega a la carpeta donde están los archivos. Ejecuta:
   ```bash
   python server.py
   ```
2. **Ejecutar el Cliente TCP**  
   Abre una terminal y navega a la carpeta donde están los archivos. Ejecuta:
   ```bash
   python client.py
    ```
## Como realizar pruebas 
### Prueba 1: Enviar un mensaje normal
1. Ejecuta el servidor y luego el cliente.
2. Ingresa un mensaje normal como "hola servidor" en el cliente.
3. El servidor responderá en mayúsculas. Verifica que la respuesta sea "HOLA SERVIDOR".

### Prueba 2: Desconexion
1. Ingresa la palabra "DESCONEXION" en el cliente.
2. Verifica que el cliente cierre la conexión con el servidor y termine su ejecución.
3. El servidor debe seguir disponible para aceptar nuevas conexiones.

## Ejemplos de pruebas realizadas 
### Consola del cliente
```bash
PS D:\tcp> python client.py
Se establece una conexión con el servidor.
Ingresa mensaje (o 'DESCONEXION' para salir): HOLA MICHAEL
Respuesta del servidor: HOLA MICHAEL
Ingresa mensaje (o 'DESCONEXION' para salir): otro mensaje
Respuesta del servidor: OTRO MENSAJE
Ingresa mensaje (o 'DESCONEXION' para salir): todo ok
Respuesta del servidor: TODO OK
Ingresa mensaje (o 'DESCONEXION' para salir): DESCONEXION
Cerrando conexión con el servidor...
PS D:\tcp> python client.py
Se establece una conexión con el servidor.
Ingresa mensaje (o 'DESCONEXION' para salir): de nuevo por aqui
Respuesta del servidor: DE NUEVO POR AQUI     
Ingresa mensaje (o 'DESCONEXION' para salir): hola  
Respuesta del servidor: HOLA 
Ingresa mensaje (o 'DESCONEXION' para salir): prueba           
Respuesta del servidor: PRUEBA
Ingresa mensaje (o 'DESCONEXION' para salir): DESCONEXION
Cerrando conexión con el servidor...
PS D:\tcp>    
```
### Consola del servidor
```bash
PS D:\tcp> python server.py
Servidor TCP en esperando conexiones en 127.0.0.1:5000
Conexión establecida con el cliente ('127.0.0.1', 25875)
Mensaje recibido: HOLA MICHAEL
Respuesta enviada al cliente: HOLA MICHAEL
Mensaje recibido: otro mensaje
Respuesta enviada al cliente: OTRO MENSAJE
Mensaje recibido: todo ok
Respuesta enviada al cliente: TODO OK
Mensaje recibido: DESCONEXION
El cliente ('127.0.0.1', 25875) solicita desconexión.
Conexión establecida con el cliente ('127.0.0.1', 5147)
Mensaje recibido: de nuevo por aqui
Respuesta enviada al cliente: DE NUEVO POR AQUI
Mensaje recibido: hola 
Respuesta enviada al cliente: HOLA 
Mensaje recibido: prueba
Respuesta enviada al cliente: PRUEBA
Mensaje recibido: DESCONEXION
El cliente ('127.0.0.1', 5147) solicita desconexión.

```

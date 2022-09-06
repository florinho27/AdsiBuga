""" host = 'localhost'
port = 3306
import socket

obj = socket.socket()
obj.connect ( (host , port) )
print("Conectado al servidor")


while True:
    mens = input("Mensaje desde Cliente a Servidor >> ")

    obj.send(mens.encode('ascii'))
    recibido = obj.recv(1024)
    print(recibido)

    obj.close() """
    #Se importa el módulo
host = 'localhost'
port = 3306
#Se importa el módulo
import socket

#Creación de un objeto socket (lado cliente)
obj = socket.socket()

#Conexión con el servidor. Parametros: IP (puede ser del tipo 192.168.1.1 o localhost), Puerto
obj.connect((host, port))
print("Conectado al servidor")

#Creamos un bucle para retener la conexion
while True:
#Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
    mens = input("Mensaje desde Cliente a Servidor >> ")
    #Con el método send, enviamos el mensaje
    obj.send(mens.encode('ascii'))
    #obj.send(mens)
    recibido = obj.recv(1024)
    print(recibido)

    #Cerramos la instancia del objeto servidor
    obj.close()

    #Imprimimos la palabra Adios para cuando se cierre la conexion
    print("Conexión cerrada")
import socket

ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ser.bind(("", 3306))

ser.listen(7)


cli, addr = ser.accept()

while True:

    recibido = cli.recv(1024)

    print("Recibo conexion de la IP: " + str(addr[0]) + " Puerto: " + str(addr[1]))
    print(recibido)

    msg_toSend=("mensaje recibido desde el cliente como estas Jerry")
    cli.send(msg_toSend.encode('ascii'))

    cli.close()
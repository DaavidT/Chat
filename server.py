import socket
import select
import sys
from threading import Thread

host = "127.0.0.1"
port = 1234
server = sockect.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(sockect.SOL_SOCKET, socket.SO_REUSEADOR, 1)
server.bind((ip, port))
server.listen(10)
list_of_clients = []


def cliente_thread(conn, addr):
    conn.send("Bienvenido al chat")

    while True:
        try:
            message = conn.recv(1024)
            if message:
                print("<" + addr[0])

                message_to_send = "<" + addr[0] + ">" + message
            else:
                remove(conn)
        except:
            pass


try:
    message = conn.recv(1024)
    while True:
        print("<" + addr[0])
        message_to_send = "<" + addr[0] + ">" + message
        if message == 'salir':
            break
    server.close()
except:
    server.close()


def remove(connection)
   if connection in list_of_clients:
        list_of_clients.remove(connection)

    while True:
        conn, addr = server. accept()

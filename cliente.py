import socket
import select
import sys
import threading
import pickle


class Cliente():
    def __init__(server, host="127.0.0.1", port=1234):
        username = input("Username: ")

        server.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.sock.connect((str(host), int(port)))
        server.send_usuario(username + "_user")
        msg_rcv = threading.Thread(target=server.msg_rcv)

        msg_rcv.daemon = True
        msg_rcv.start()
        while True:
            msg = input(f'{username} > ')
            if msg != 'salir':
                server.send_msg(msg)
            else:
                server.sock.close()
                sys.exit()

    def msg_rcv(server):
        while True:
            try:
                data = server.sock.recv(1024)
                if data:
                    print(" ")
                    print('Mensaje nuevo:')
                    print(data.decode('utf-8'))
            except:
                pass

    def send_msg(server, msg):
        print('Mensaje enviado')
        mensaje = msg.encode('utf-8')
        server.sock.send(mensaje)

    def send_usuario(server, username):
        print('Usuario enviado')
        server.sock.send(username.encode('utf-8'))


c = Cliente()

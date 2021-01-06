import socket
import select
import sys
import threading
import pickle


class Cliente():
    def __init__(server, host="127.0.0.1", port=1234):
        server.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.sock.connect((str(host), int(port)))

        msg_rcv = threading.Thread(target=server.msg_rcv)

        msg_rcv.daemon = True
        msg_rcv.start()
        while True:
            msg = input('Manda un mensaje: ')
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
                    print(pickle.loads(data))
            except:
                pass

    def send_msg(server, msg):
        print('Mensaje enviado')
        server.sock.send(pickle.dumps(msg))


c = Cliente()

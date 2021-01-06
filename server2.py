import socket
import threading
import sys
import pickle


class Servidor():

    def __init__(server, host="127.0.0.1", port=1234):

        server.list_of_clients = []

        server.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.sock.bind((str(host), int(port)))
        server.sock.listen(10)
        server.sock.setblocking(False)

        aceptar = threading.Thread(target=server.aceptar_con)
        procesar = threading.Thread(target=server.procesar_con)

        aceptar.daemon = True
        aceptar.start()
        procesar.daemon = True
        procesar.start()

        while True:
            msg = input('->')
            if msg == 'salir':
                server.sock.close()
                sys.exit()
            else:
                pass

    def msg_all(server, msg, cliente):
        for c in server.list_of_clients:
            try:
                if c != cliente:
                    c.send(msg)
            except:
                pass

    def aceptar_con(server):
        print("Servidor iniciado")
        while True:
            try:
                conn, addr = server.sock.accept()
                conn.setblocking(False)
                server.list_of_clients.append(conn)
                print(server.list_of_clients)
            except:
                pass

    def procesar_con(server):
        while True:
            for c in server.list_of_clients:
                try:
                    data = c.recv(1024)
                    if data:
                        print(" ")
                        print('Mensaje recibido y enviado')
                        server.msg_all(data, c)
                except:
                    pass


s = Servidor()

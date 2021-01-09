import socket
import threading
import sys
import pickle


class Servidor():

    def __init__(server, host="127.0.0.1", port=1234):
        server.list_of_clients = []
        server.list_of_usernames = {}

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
                    msgg_final = server.list_of_usernames[cliente] + ": " + msg
                    c.send(msgg_final.encode('utf-8'))
                    # c.send(msg.encode('utf-8'))
            except:
                pass

    def mensaje_especifico(server, msg, cliente, send, nombre):
        for c in server.list_of_clients:
            try:
                if c == cliente:
                    print('Entre al if')
                    msgg_final = nombre + ": " + msg
                    print(msgg_final)
                    c.send(msgg_final.encode('utf-8'))
            except Exception as e:
                print(Exception)
                sys.exit()

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
                        print(data.decode('utf-8'))
                        if '_user' in data.decode('utf-8'):
                            underscore = data.decode('utf-8').find('_user')
                            server.list_of_usernames[data.decode(
                                'utf-8')[0:underscore]] = c
                            print(server.list_of_usernames)
                            continue
                        elif data.decode('utf-8').find("/") == 0:
                            print('Estoy funcionando')
                            space = data.decode('utf-8').find(" ")
                            nombre = data.decode('utf-8')[1:space]
                            mensaje_spf = data.decode('utf-8')[space + 1:]
                            print('Antes')
                            print(server.list_of_usernames[nombre])
                            server.mensaje_especifico(
                                mensaje_spf, server.list_of_usernames[nombre], c, nombre)
                            print('Despues')
                        else:
                            print(" ")
                            print('Mensaje para todos')
                            server.msg_all(data.decode('utf-8'), c)
                except WindowsError:
                    pass
                except Exception as e:
                    print(e)


s = Servidor()

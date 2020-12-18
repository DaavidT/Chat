import socket


def init_server():
    print("Iniciando servidor...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 1234))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print("Conectado por", addr)
            while True:
                data = s.recv(1024)
                conn.sendall(data)


if __name__ == "__main__":
    init_server()

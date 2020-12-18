import socket

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 1234
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"Hello world")
        data = s.recv(1024)
    print("Recibido", repr(data))

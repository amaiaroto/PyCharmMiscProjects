import socket
from threading import Thread
name = input("What is your name? (will be displayed when you type a message)\n")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(("0.0.0.0", 5000))
    server_socket.listen(5)
    print(222)
    conn, adrs = server_socket.accept()
    def a():
        while True:
            conn.send((name + ": " + input()).encode("ascii"))
    t=Thread(target=a)
    t.start()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                try:
                    st = data.decode("ascii")
                    print(st)
                except ValueError:
                    pass



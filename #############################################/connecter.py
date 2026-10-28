import socket

name = input("What is your name? (will be displayed when you type a message)\n")
conn = input("What IPv4 Address would you like to connect to? (this is who your're chatting with)\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((conn, 8080))

except OSError | WindowsError:
    exit("Failed to connect")

while True:
    s.send((name+": "+input()).encode())
    print(s.recv(1024).decode())

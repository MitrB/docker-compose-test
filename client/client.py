import socket
import time

HOST = "server"
PORT = 12345

time.sleep(2)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for i in range(5):
        message = f"Hello {i}"
        s.sendall(message.encode())
        print("Sent:", message)
        time.sleep(1)


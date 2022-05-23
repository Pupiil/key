#!/usr/bin/env python3

import socket
from cryptography.fernet import Fernet

HOST = "127.52.0.2"  # Standard loopback interface address (localhost)
PORT = 6000  # Port to listen on (non-privileged ports are > 1023)
fernet: Fernet = Fernet(Fernet.generate_key())

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        print(f"[KEY::KEY] Starting connection to {HOST}, {PORT}")        

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"[KEY] Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    conn.sendall(fernet._signing_key + b"|" + fernet._encryption_key)

if __name__ == '__main__':
    main()

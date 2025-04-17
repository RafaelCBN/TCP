import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 65433
BUFFER_SIZE = 1024

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(BUFFER_SIZE)
            if not data:
                print("Conexão encerrada pelo servidor.")
                sock.close()
                sys.exit()
            print(data.decode('utf-8'), end='')
        except:
            print("Erro ao receber dados.")
            sock.close()
            sys.exit()

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        print(f"Conectado ao servidor {HOST}:{PORT}")

        thread = threading.Thread(target=receive_messages, args=(s,))
        thread.daemon = True
        thread.start()

        while True:
            message = input()
            s.send(message.encode('utf-8'))
            if message == '/quit':
                break

        s.close()
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()

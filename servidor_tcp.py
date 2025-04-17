import socket

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço de loopback (localhost)
PORT = 65432        # Porta para escutar (não privilegiada)

try:
    # Criação do socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"Servidor escutando em {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Conectado por {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Recebido: {data.decode('utf-8')}")
                    conn.sendall(f"Eco: {data.decode('utf-8')}".encode('utf-8'))
                print(f"Conexão com {addr} encerrada")
except KeyboardInterrupt:
    print("\nServidor encerrado pelo usuário")
except Exception as e:
    print(f"Erro: {e}")

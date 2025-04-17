import socket

# Configurações do cliente
HOST = '127.0.0.1'  # Endereço do servidor
PORT = 65432        # Porta do servidor

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Conectado ao servidor {HOST}:{PORT}")

        while True:
            message = input("Digite uma mensagem (ou 'sair' para encerrar): ")
            if message.lower() == 'sair':
                break
            s.sendall(message.encode('utf-8'))
            data = s.recv(1024)
            print(f"Resposta do servidor: {data.decode('utf-8')}")

        print("Conexão encerrada")
except ConnectionRefusedError:
    print("Erro: Não foi possível conectar ao servidor. Verifique se ele está rodando.")
except Exception as e:
    print(f"Erro: {e}")

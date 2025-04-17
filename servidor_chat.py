import socket
import threading

HOST = '127.0.0.1'
PORT = 65433  # Porta diferente da usada anteriormente para evitar conflito

clientes = []

# Função para transmitir a mensagem a todos os clientes conectados
def broadcast(mensagem, cliente_remetente):
    for cliente in clientes:
        if cliente != cliente_remetente:
            try:
                cliente.send(mensagem)
            except:
                cliente.close()
                if cliente in clientes:
                    clientes.remove(cliente)

# Função para lidar com a conexão individual de cada cliente
def handle_client_connection(client_socket, addr):
    print(f">>> Conexão de {addr}")
    try:
        nome = client_socket.recv(1024).decode()
        mensagem_boas_vindas = f">>> {nome} entrou no chat <<<\n"
        print(mensagem_boas_vindas.strip())
        broadcast(mensagem_boas_vindas.encode(), client_socket)

        while True:
            mensagem = client_socket.recv(1024)
            if not mensagem:
                break
            broadcast(f"{nome}: {mensagem.decode()}".encode(), client_socket)
    except:
        pass
    finally:
        print(f">>> {nome} saiu do chat <<<")
        broadcast(f">>> {nome} saiu do chat <<<\n".encode(), client_socket)
        clientes.remove(client_socket)
        client_socket.close()

# Função principal do servidor
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Servidor de chat rodando em {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        clientes.append(client_socket)
        thread = threading.Thread(target=handle_client_connection, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    main()

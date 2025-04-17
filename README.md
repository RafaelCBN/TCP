Atividade 1 – Comunicação TCP básica
Foram criados dois programas: servidor_tcp.py e cliente_tcp.py. O servidor aguardava conexões e respondia com uma mensagem "eco" para qualquer dado recebido do cliente. Foi realizada a análise dos pacotes trocados usando o Wireshark.

Atividade 2 – Chat com múltiplos clientes
Foram implementados servidor_chat.py e cliente_chat.py. O servidor utilizava threads para lidar com múltiplas conexões simultâneas. As mensagens enviadas por um cliente eram retransmitidas a todos os outros. Houve a necessidade de resolver erros como conflitos de porta e nome de função ausente.

Atividade 3 – Melhorias no cliente de chat
O cliente foi aprimorado no arquivo cliente_chat_melhorado.py, adicionando comandos como "sair" para encerrar a conexão, além de mensagens automáticas notificando a entrada e saída dos usuários.

Atividade 4 – Testes de resiliência
Foi criado o arquivo testes_resiliencia.py para simular falhas, como queda de conexão ou desligamento de clientes, testando a estabilidade e o comportamento do servidor sob condições adversas.


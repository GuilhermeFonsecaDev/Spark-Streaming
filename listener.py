import socket 
import time

HOST = 'localhost'
PORT = 8080


# O SOCKET É RESPONSÁVEL POR ESTABELECER A CONEXÃO ENTRE O CLIENTE E O SERVIDOR, PERMITINDO A TRANSMISSÃO CONTÍNUA DE DADOS EM TEMPO REAL.

s = socket.socket() # CRIA O SOCKET

s.bind((HOST,PORT)) # CONECTA O HOST E A PORTA COM O SOCKET 
print(f'Aguardando solicitação na porta {PORT}')


# O "LISTEN" É RESPONSÁVEL POR AGUARDAR CONEXÕES DE CLIENTES EM UMA PORTA ESPECÍFICA E PERMITIR QUE O SERVIDOR ESTABELEÇA UMA CONEXÃO PARA TRANSMITIR DADOS EM TEMPO REAL.

s.listen(5) # O PARÂMETRO ESPECIFICA O NÚMERO MÁXIMO DE CONEXÕES EM ESPERA QUE O SERVIDOR PODE TER EM SUA FILA DE CONEXÕES PENDENTES
conn, address = s.accept()
print(f'Recebendo solicitação de {address}')

messages = [
   'Mensagem A',
     'Mensagem B',
     'Mensagem C',
     'Mensagem D',
     'Mensagem E',
     'Mensagem F',
     'Estou animado com o curso'
     ]


for message in messages:
    message = bytes(message, 'utf-8')
    conn.send(message)
    time.sleep(5)

conn.close()


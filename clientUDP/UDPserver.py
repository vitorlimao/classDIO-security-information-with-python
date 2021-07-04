import socket
#Cria um objeto de conexão Socket, acessa a biblioteca do socket
# e acessa aos métodos de IPV4(AF_INET) e UDP(sockDGRAM)

conexao=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print("Socket criado com sucesso!!!")

host='localhost'
port=5432

conexao.bind((host,port))#bind faz a ligação entre cliente e servidor através do host e da porta
mensagem="Dale louco!"

while 1:
    dados,endereço = conexao.recvfrom(4096)
    #faz uma ligação e devolve resposta enquanto for verdadeira o próprio bin
    #retorna True quando dá certo e false quando não.
    if dados:
        print ('Servidor enviando mensagem...')
        conexao.sendto(dados + (mensagem.encode()), endereço)
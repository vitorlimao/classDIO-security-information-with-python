import socket


conexao:socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print("Cliente Socket criado com sucesso!!!")

host='localhost'
porta='5433'
mensagem="Olá servidor!!"

try:
    print ("Client: "+ mensagem)
    conexao.sendto(mensagem.encode(),(host,5432)) #envia os dados empacotados pro servidor na porta 54,2

    dados, servidor = conexao.recvfrom(4096) #esperando a reposta do servidor
    dados = dados.decode() #desempacota
    print("Cliente: "+ dados)
finally:
    print("Cliente: fechando conexão. ")
    conexao.close()


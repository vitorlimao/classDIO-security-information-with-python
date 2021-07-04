import socket

import sys


def main():
    try:
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM,
                                0)  # cria um objeto do tipo socket, informa os protocolos e comunicação que serão usados
    except socket.error as error:
        print("conexão falhou")
        print("Error.{}".format(error))
        sys.exit()
    print("socket criado com sucesso")

    hostAlvo = input("Digite o host ou Ip a ser conectado: ")
    portAlvo = input("Digite a porta a ser conectada: ")

    try:  # ligar conexao
        conexao.connect((hostAlvo, int(portAlvo)))

        print("Cliente TCP conectado com sucesso no host Alvo: " + hostAlvo + "na porta: " + portAlvo)
        # espera dois segundos para encerrar a conexão
        conexao.shutdown(2)

    except socket.error as error:
        print("Não foi possível conectar no host: " + hostAlvo + "na porta: " + portAlvo)
        print("Erro: {}".format(error))
        sys.exit()


if __name__ == "__main__":
    main()

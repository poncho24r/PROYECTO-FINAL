from socket import *
import logging

logging.basicConfig(filename='ser.log', encoding='utf-8', level=logging.INFO)

def hola():
    direccionServidor = "localhost"
    puertoServidor = 9099

    socketServidor = socket(AF_INET, SOCK_STREAM)

    socketServidor.bind((direccionServidor, puertoServidor))

    socketServidor.listen()

    
          
    while True:
        socketConexion, addr = socketServidor.accept()
        print("Conectado con un Cliente",addr)

        while True:
            mensajeRecibido = socketConexion.recv(4096).decode()
            print(mensajeRecibido)
            logging.info(mensajeRecibido)


            if mensajeRecibido == 'adios':
                  break


            socketConexion.send(input().encode())


        print("Desconectado el cliente", addr)

        socketConexion.close()
        exit()
            

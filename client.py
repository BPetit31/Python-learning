import socket
connexionServeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexionServeur.connect(('localhost', 12800))

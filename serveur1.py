import socket

connexionPrincipale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexionPrincipale.bind(('', 12800))
connexionPrincipale.listen(5)
connexion_avec_client, infos_connexion = connexionPrincipale.accept()






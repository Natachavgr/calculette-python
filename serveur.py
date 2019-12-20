import socket
import os
from division import *


hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()
valeur_recu1=int(connexion_avec_client.recv(1024))
valeur_recu2=int(connexion_avec_client.recv(1024))

valeurfinal_recu=division(valeur_recu1,valeur_recu2)
connexion_avec_client.send(str(valeurfinal_recu).encode())
 
print("La valeur de la division :",valeur_recu1,"/",valeur_recu2,"=",valeurfinal_recu)



print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()


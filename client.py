import socket
import os
from division import * 

hote = "localhost"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))


a =input("Entrez le premier nombre : ")
b =input("Entrez le deuxieme nombre : ")

a= a.encode()
b= b.encode()
connexion_avec_serveur.send(a)
connexion_avec_serveur.send(b)

valeurfinal_recu=connexion_avec_serveur.recv(1024)
print("La valeur de la division :",a.decode() ,"/",b.decode(),"=",valeurfinal_recu.decode())




print("Fermeture de la connexion")
connexion_avec_serveur.close()
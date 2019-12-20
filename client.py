import socket

if __name__ == "__main__":
    HOST="localhost"
    PORT=50007
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((HOST, PORT))
    valeur_1 = input("Saisir chiffre 1 ")
    signe = input("Saisir signe")
    valeur_2 = input("Saisir chiffre 2 ")

    socket.send(valeur_1.encode())
    socket.send(signe.encode())
    socket.send(valeur_2.encode())

    result = socket.recv(1024).decode()

    print("Le resultat de l'operation {}".format(result))

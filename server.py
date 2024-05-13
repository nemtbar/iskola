import threading
from cloud.sending import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 8080))
clients = []


def handle(client):
    run = True
    while run:
        msg = recv(client)
        print(msg)
        if msg == "quit":
            send(client, "quit")
            client.close()
            run = False
            break
        else:
            for i in clients:
                if i != client:
                    send(i, msg)


def main():
    server.listen()
    run = True
    while run:
        cli, addr = server.accept()
        clients.append(cli)
        threading.Thread(target=handle, args=(cli,)).start()


main()

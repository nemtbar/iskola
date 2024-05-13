from cloud.sending import *
import threading
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = input("name: ")


def handle(conn: socket.socket):
    run = True
    while run:
        msg = recv(conn)
        if msg == "quit":
            conn.close()
            run = False
            break
        print(msg)


def main():
    run = True
    client.connect(('localhost', 8080))
    threading.Thread(target=handle, args=(client,)).start()
    while run:
        msg = input("")
        if msg == "quit":
            send(client, msg)
            run = False
        else:
            send(client, f"{name}:{msg}")

#büdi
main()

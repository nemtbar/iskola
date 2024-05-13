import socket

HEADER = 64


def send(conn: socket.socket, msg: str):
    msg = msg.encode("utf-8")
    size = str(len(msg)).encode("utf-8")
    size += b" " * (HEADER-len(size))
    conn.send(size)
    conn.send(msg)


def recv(conn: socket.socket) -> str:
    size = conn.recv(HEADER).decode("utf-8").strip()
    if size != "":
        size = int(size)
        msg = conn.recv(size).decode("utf-8")
        return msg
    else:
        return ""


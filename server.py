import socket
from _thread import *

import pickle

server = "192.168.0.108"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")

DATA = []

def threaded_client(conn, player):
    conn.send(pickle.dumps(1))
    reply = {}
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            # players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if data not in DATA:
                    DATA.append(data)
                reply = DATA
                
                    

                # print("Received: ", data)
                # print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1

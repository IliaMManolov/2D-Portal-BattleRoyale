import socket
import json

def initMain(prevGameState):
    gameState = prevGameState
    gameState["selectedOption"] = "Start game"
    gameState["stage"] = 0
    gameState["mousePosition"] = (0, 0)
    gameState["running"] = True

    return gameState


def initGame(prevGameState, serverIP, port = 9001):
    gameState = prevGameState
    gameState["myIP"] = socket.gethostbyname(socket.gethostname())
    gameState["serverIP"] = serverIP
    gameState["port"] = port
    gameState["stage"] = 1

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((serverIP, port))

    s.send("connect_player")
    data = s.recv(1024)
    gameState["socket"] = s
    gameState = {**gameState, **(json.loads(data))}   # Merge gameState and data

    return gameState
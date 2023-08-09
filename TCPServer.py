from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode().strip()
    print(sentence)
    response = ""
    sentence_partitions = sentence.split(":")
    numberOfInputs = len(sentence_partitions)
    if sentence == "STOP":
        response = "STOPPING"
    elif sentence.startswith("ADD") and numberOfInputs == 3:
        response = "OK"
    elif not sentence.startswith("ADD"):
        response = "ILLEGAL REQUEST"
    elif numberOfInputs != 3:
        response = "ILLEGAL ADD"
    connectionSocket.send(response.encode())
    connectionSocket.close()
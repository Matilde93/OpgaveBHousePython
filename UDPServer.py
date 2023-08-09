from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print('Server is ready to listen')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    decodedMessage = message.decode()
    print(decodedMessage)
    response = ""
    sentence_partitions = str(message).split(":")
    numberOfInputs = len(sentence_partitions)
    if decodedMessage == "STOP":
        response = "STOPPING"
    elif decodedMessage.startswith("ADD") and numberOfInputs == 3:
        response = "OK"
    elif not decodedMessage.startswith("ADD"):
        response = "ILLEGAL REQUEST"
    elif numberOfInputs != 3:
        response = "ILLEGAL ADD"
    serverSocket.sendto(response.encode(), clientAddress)

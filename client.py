from socket import *
import sys

def main():
    #check if there are five arguments including the file name, the n_port cannot exceed 65535
    if len(sys.argv) == 5 and int(sys.argv[2]) <= 65535:
        #set up connection to n_port
        serverName = sys.argv[1]
        serverPort = int(sys.argv[2])
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName,serverPort))

        #send request code
        requestCode = sys.argv[3]
        clientSocket.send(requestCode.encode())

        #try except to check if server closed due to wrong request code
        try:
            rPort = int(clientSocket.recv(1024).decode())
            # print(rPort)
            clientSocket.close()

            # #UDP, send message and recieve reserved message
            clientSocket = socket(AF_INET,SOCK_DGRAM)
            clientSocket.sendto(sys.argv[4].encode(),(serverName,rPort))
            modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
            print(modifiedMessage.decode())
            clientSocket.close()
        except:
            clientSocket.close()

main()
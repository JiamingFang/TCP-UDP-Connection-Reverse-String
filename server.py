from socket import *
import random
import sys

def reverse(s):
    return s[::-1]

def main():
    #check number of argument is 2, which includes file name
    if len(sys.argv) == 2:
        serverPort = 12001
        serverSocket = socket(AF_INET, SOCK_STREAM)

        #check port is not taken, if taken increment by 1
        while True:
            try:
                serverSocket.bind(('',serverPort))
                break
            except:
                serverPort += 1
        serverSocket.listen(1)
        print("SERVER_PORT="+str(serverPort))

        #allow continue listening to n_port
        while True:
            connectionSocket,addr = serverSocket.accept()
            requestCode = connectionSocket.recv(1024).decode()

            #check request code from client is correct
            if requestCode == sys.argv[1]:
                # #UDPserver
                serverSocket2 = socket(AF_INET,SOCK_DGRAM)

                #check that random r_port is not taken
                while True:
                    rPort = str(random.randint(1025,60001))
                    try:
                        serverSocket2.bind(("",int(rPort)))
                        break
                    except:
                        # print("r_port is taken")
                        pass

                #send r_port and close connection socket
                connectionSocket.send(rPort.encode())
                connectionSocket.close()

                #get message, reverse and send back
                message, clientAddress = serverSocket2.recvfrom(1024)
                modifiedMessage = reverse(message.decode())
                serverSocket2.sendto(modifiedMessage.encode(),clientAddress)
                serverSocket2.close()

            #if request code not correct, print exception
            else:
                connectionSocket.close()
                serverSocket.close()
                # print("Request Code Exception")
                break

main()
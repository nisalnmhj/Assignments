#Name: Nishan Maharjan
#Section: 03
#Date: 3/7/24
#Description: Client sends " PING" to server. Server generates random to number to keep or ignore the "PING" messa#ge sent from client. If kept, server responds "PONG" else "Time out" 
#Import Libraries
from socket import *
import sys
import random # to generate a random number for packet loss

#This function creates server with a given port number. Port number is 8001
def create_server(port ):
    #using AF_INET and SOCK_DGRAM
    svr_socket = socket(AF_INET, SOCK_DGRAM)
    svr_socket.bind(("0.0.0.0", port ))
    print(f"Server listening on port 8001")
    while True:
        response = "PONG"
        data, cli_address = svr_socket.recvfrom(2048) #Server receives message from Client
        messageReceived = data.decode()

        if random.random() < 0.3: # random number determines packet loss or not
            print("packet loss - Message dropped. ")
            svr_socket.sendto(" Requested time out".encode(), cli_address)# Time out message sent to Client as packet has been lost
        else:
            print(f"Received {cli_address}:{messageReceived}")       
            svr_socket.sendto(response.encode(), cli_address) # PONG response sent to Client

def main():
    if len(sys.argv) != 2:
        print("Usage: python plingsvr.py <port>")
        sys.exit(1)
    port = int(sys.argv[1])
    create_server(port )

if __name__ == "__main__":
    main()

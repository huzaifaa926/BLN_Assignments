#!/usr/bin/env python3

# Importing libraries
import socket
import sys

# Lets catch the 1st argument as server ip
def get_command_line_argument():
    if (len(sys.argv) > 1):
        return sys.argv[1]
    else:
        print("\n\n Run like \n python3 client.py < serverip address > \n\n")
        exit(1)


def send_file_to_server(ServerIp, PORT, filename, fileMode, bytesToBeSend):
    # Now we can create socket object
    s = socket.socket()
    # Lets connect to that port where server may be running
    s.connect((ServerIp, PORT))
    # We can send file sample.txt
    file = open(filename, fileMode)
    SendData = file.read(bytesToBeSend)
    while SendData:
        # Now we can receive data from server
        print("\n\n################## Below message is received from server ################## \n\n ", s.recv(bytesToBeSend).decode("utf-8"))
        #Now send the content of sample.txt to server
        s.send(SendData)
        SendData = file.read(bytesToBeSend)      
    # Close the connection from client side
    s.close()

if __name__ == "__main__":
    ServerIp = get_command_line_argument()
    # Lets choose one port and connect to that port
    PORT = 9899
    send_file_to_server(ServerIp, PORT, 'sample.txt', 'rb', 1024)
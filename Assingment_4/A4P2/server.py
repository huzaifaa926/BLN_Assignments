#!/usr/bin/env python3

# Importing socket library 
import socket


def get_file_from_client(PORT, filename, fileMode, bytesToBeRecv):
    # Now we can create socket object
    s = socket.socket()
    # Lets choose one port and start listening on that port
    print("\n Server is listing on port :", PORT, "\n")
    # Now we need to bind to the above port at server side
    s.bind(('', PORT))
    # Now we will put server into listenig  mode 
    s.listen(10)
    #Open one recv.txt file in write mode
    file = open(filename, fileMode) 
    print(f"\n Copied file name will be {filename} at server side\n")
    # Now we do not know when client will concatct server so server should be listening contineously  
    while True:
        # Now we can establish connection with clien
        conn, addr = s.accept()
        # Send a hello message to client
        msg = "\n\n|---------------------------------|\n Hi Client[IP address: "+ addr[0] + "], \n ֲֳ**Welcome to Server** \n -Server\n|---------------------------------|\n \n\n"    
        conn.send(msg.encode())
        # Receive any data from client side
        RecvData = conn.recv(bytesToBeRecv)
        while RecvData:
            file.write(RecvData)
            RecvData = conn.recv(bytesToBeRecv)
        # Close the file opened at server side once copy is completed
        file.close()
        print("\n File has been copied successfully \n")
        # Close connection with client
        conn.close()
        print("\n Server closed the connection \n")

        # Come out from the infinite while loop as the file has been copied from client.
        break

if __name__ == "__main__":
    get_file_from_client(9899, "recv.txt", "wb", 1024)
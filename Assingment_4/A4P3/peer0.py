#!/usr/bin/env python3

# Importing socket library 
import socket
import sys

# Lets catch the 1st argument as Peer ip
def get_command_line_argument():
    if (len(sys.argv) > 1):
        return sys.argv[1]
    else:
        return "peer acting as a server"
        # print("\n\n Run like \n python3 peer.py < Peerip address > \n\n")
        # exit(1)


def send_file_to_peer(PeerIp, PORT, filename, fileMode, bytesToBeSend):
    # Now we can create socket object
    s = socket.socket()
    # Lets connect to that port where Peer may be running
    s.connect((PeerIp, PORT))
    # We can send file sample.txt
    file = open(filename, fileMode)
    SendData = file.read(bytesToBeSend)
    while SendData:
        # Now we can receive data from Peer
        print("\n\n################## Below message is received from Peer ################## \n\n ", s.recv(bytesToBeSend).decode("utf-8"))
        #Now send the content of sample.txt to Peer
        s.send(SendData)
        SendData = file.read(bytesToBeSend)      
    # Close the connection from peer side
    s.close()


def get_file_from_peer(PORT, filename, fileMode, bytesToBeRecv):
    # Now we can create socket object
    s = socket.socket()
    # Lets choose one port and start listening on that port
    print("\n Peer is listing on port :", PORT, "\n")
    # Now we need to bind to the above port at Peer side
    s.bind(('', PORT))
    # Now we will put Peer into listenig  mode 
    s.listen(10)
    #Open one recv.txt file in write mode
    file = open(filename, fileMode) 
    print(f"\n Copied file name will be {filename} at Peer side\n")
    # Now we do not know when peer will concatct Peer so Peer should be listening contineously  
    while True:
        # Now we can establish connection with peer
        conn, addr = s.accept()
        # Send a hello message to peer
        msg = "\n\n|---------------------------------|\n Hi peer[IP address: "+ addr[0] + "], \n ֲֳ**Welcome to Peer** \n -Peer\n|---------------------------------|\n \n\n"    
        conn.send(msg.encode())
        # Receive any data from peer side
        RecvData = conn.recv(bytesToBeRecv)
        while RecvData:
            file.write(RecvData)
            RecvData = conn.recv(bytesToBeRecv)
        # Close the file opened at Peer side once copy is completed
        file.close()
        print("\n File has been copied successfully \n")
        # Close connection with peer
        conn.close()
        print("\n Peer closed the connection \n")

        # Come out from the infinite while loop as the file has been copied from peer.
        break

if __name__ == "__main__":
    # Lets choose one port and connect to that port
    PORT = 9899
    PeerIp = get_command_line_argument()
    if PeerIp == "peer acting as a server":
        get_file_from_peer(PORT, "recv.txt", "wb", 1024)
    else:
        send_file_to_peer(PeerIp, PORT, 'sample.txt', 'rb', 1024)
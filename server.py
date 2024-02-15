#imports
import socket
# import threading
# import cv2
# import pickle
# import imutils
# import time
import struct

#constants
HOST = socket.gethostname()
HOST_IP = socket.gethostbyname(HOST)
PORT = 8080
ADDR = (HOST_IP,PORT)
FORMAT = "utf-8"
PAYLOAD_SIZE = struct.calcsize("Q")#Q is format for long long int btw --> 8 bytes on most platforms
# THREAD_COUNT = 0
# MAX_THREADS = 5
MAX_CONNECTIONS =  5

#server
def start_server():
    global THREAD_COUNT
    
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    print(f"[SERVER]\nHOST:{HOST}\nHOST IP:{HOST_IP}\n\n")
    
    try:
        server.bind(ADDR)
        print("[BIND] Success!\n")
    except socket.error as err:
        print(str(err))
    
    print("[WAITING] Waiting for New Connections ...\n")
    print(f"[LISTENING] on PORT NO:{PORT}\n")
    
    client_data = {}
    connection_count =  0
    
    while True:
        data, addr = server.recvfrom(PAYLOAD_SIZE)
        if not data:
            break

        if connection_count >= MAX_CONNECTIONS:
            print(f"[LIMIT REACHED] Maximum number of connections ({MAX_CONNECTIONS}) reached.")
            continue
        
        if addr not in client_data:
            connection_count += 1
            print(f"[NEW CONNECTION] from {addr}.\n")
            client_data[addr] = []
        client_data[addr].append(data)

        print(f"Received message: {data} from {addr}")
        
        for client_addr, client_messages in client_data.items():
                for message in client_messages:
                    server.sendto(message, client_addr)


       
start_server()
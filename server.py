#imports
import socket
# import threading
import cv2
import pickle
# import imutils
import time
import struct

#constants
HOST = socket.gethostname()
HOST_IP = socket.gethostbyname(HOST)
PORT = 8080
ADDR = (HOST_IP,PORT)
FORMAT = "utf-8"
PAYLOAD_SIZE = 2048
# THREAD_COUNT = 0
# MAX_THREADS = 5
MAX_CONNECTIONS =  5


#accept gracious termination


#server
def start_server():
    # global THREAD_COUNT
    
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    print(f"[SERVER]\nHOST:{HOST}\nHOST IP:{HOST_IP}\n\n")
    
    try:
        server.bind(ADDR)
        print("[BIND] Success!\n")
    except socket.error as err:
        print(str(err))
        return
    
    print("[WAITING] Waiting for New Connections ...\n")
    print(f"[LISTENING] on PORT NO:{PORT}\n")
    
    client_data = {}
    connection_count =  0
    client_connections = {}

    while True:
        try:
            data, addr = server.recvfrom(PAYLOAD_SIZE)
        except ConnectionResetError:
            print(f"[CONNECTION RESET] {addr} has disconnected.")
            continue
        
        if not data:
            # Client has disconnected
            if addr in client_connections and client_connections[addr]:
                client_connections[addr] = False
                print(f"[DISCONNECTED] {addr} has disconnected.")
                connection_count -= 1
            continue
        
        
        if addr not in client_connections:
            client_connections[addr] = True
            connection_count += 1
        elif client_connections.get(addr, False) == False:
            print(f"[RECONNECTED] {addr} has reconnected.")
            client_connections[addr] = True
            connection_count += 1
            
            
        #deserealizing frames
        packet_init = struct.unpack("!L",data[0:4])[0]
        packet_decoded = data[4:]
        if packet_init ==0:
            frame = packet_decoded
        else:
            frame+=packet_decoded
        try:
            if packet_init ==0 or len(frame) == PAYLOAD_SIZE:
                frame = pickle.loads(frame)
                cv2.imshow("Receiving",frame)
                cv2.waitKey(20)
        except pickle.UnpicklingError as err:
            print(f"Unable to deserealize frame:{err}")        

        if connection_count >= MAX_CONNECTIONS:
            print(f"[LIMIT REACHED] Maximum number of connections ({MAX_CONNECTIONS}) reached.")
            continue
        
        if addr not in client_data:
            print(f"[NEW CONNECTION] from {addr}.\n")
            client_data[addr] = []
            client_connections[addr] = True
        client_data[addr].append(data)

        print(f"Received message: {data} from {addr}")
        

        for client_addr, client_messages in client_data.items():
            if client_connections.get(client_addr, False):
                for message in client_messages:
                    server.sendto(message, client_addr)
       
start_server()
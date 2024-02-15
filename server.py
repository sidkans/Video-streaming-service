#imports
import socket
import threading
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
PAYLOAD_SIZE = 1024
THREAD_COUNT = -1
MAX_THREADS = 5


def handle_client(server):
    while True:
        data,addr = server.recvfrom(PAYLOAD_SIZE)
        if not data:
            print("[DISCONNECTED] Client Disconnected")
            break
        else:
            print(f"Received messages from {addr}:{data}")


#server
def start_server():
    global THREAD_COUNT
    
    server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print(f"[SERVER]\nHOST:{HOST}\nHOST IP:{HOST_IP}\n\n")
    
    try:
        server.bind(ADDR)
        print("[BIND] Success!\n")
    except socket.error as err:
        print(str(err))
    
    

    thread = threading.Thread(target=handle_client, args=(server,))
    thread.start()
    print(f"[ACTIVE THREADS]: {THREAD_COUNT}")
        



# def thread_clients(server):
#     global THREAD_COUNT
    
#     while True:
#         conn,addr = server.accept()
#         THREAD_COUNT+=1
#         if THREAD_COUNT >= MAX_THREADS:
#             print("[LIMIT] Maximum Number of Clients reached! Closing connection ...\n")
#             conn.close()
#             continue
        
#         # THREAD_COUNT+=1
#         # print(f"[ACTIVE THREADS]:{THREAD_COUNT}")

#         try:
#             while True:
#                 data = conn.recv(PAYLOAD_SIZE)
#                 if not data:
#                     break
                
        
#         except socket.error as err:
#             print(f"[EXCEPTION] {err}")
        
#         finally:
#             THREAD_COUNT-=1
#             conn.close()
#             print(f"[DISCONNECTED] Client Disconnected.\n[ACTIVE THREADS]:{THREAD_COUNT}")


        
start_server()
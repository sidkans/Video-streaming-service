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
    
    while True:

        x = server.recvfrom(65507)
        # clientip = x[1][0]
        try:
            data = x[0]
            data = pickle.loads(data)
            data = cv2.imdecode(data,cv2.IMREAD_COLOR)
            cv2.imshow('name1',data)
            if cv2.waitKey(10) == 13:
                continue
        except:
            pass

start_server()
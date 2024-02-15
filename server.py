#imports
import socket
import threading
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
PAYLOAD_SIZE = struct.calcsize("Q")#Q is format for long long int btw --> 8 bytes on most platforms

#server
def start_server():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(f"[SERVER]\nHOST:{HOST}\nHOST IP:{HOST_IP}\n\n")
    server.bind(ADDR)
    print("[BIND] Success!\n")
    server.listen(5)
    print(f"[LISTENING] on PORT NO:{PORT}\n")
    
    while True:
        conn,addr = server.accept()
        print(f"[CONNECTION] New Connection: {addr}")
        # if conn:
        #     vid = cv2.VideoCapture(0)
        #     while vid.isOpened():
        #         pass
            
            

        
start_server()
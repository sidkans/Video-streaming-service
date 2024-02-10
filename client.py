#imports
import socket
import cv2


#constants
IP = "192.168.68.103"
PORT = 8080
ADDR = (IP,PORT)
FORMAT = "utf-8"


#client
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(ADDR)

client.close()
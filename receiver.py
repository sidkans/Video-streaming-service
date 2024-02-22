#imports
import socket
import cv2
import pickle

#constants
HOST_IP = "192.168.252.240"
CLIENT_NAME = socket.gethostname()
PORT = 8080
ADDR = (HOST_IP,PORT)
FORMAT = "utf-8"
WIDTH = 640
HEIGHT = 400
PAYLOAD_SIZE = 1024


# client
def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.bind(ADDR)
    print(f"[CLIENT]\nHOST IP:{HOST_IP}\n\n")

    while True:
        try:
            data, server_address = client.recvfrom(65507)
            data = pickle.loads(data)
            data = cv2.imdecode(data, cv2.IMREAD_COLOR)
            cv2.imshow('CLIENT', data)
            if cv2.waitKey(10) == 13:
                break
        except OSError as e:
            print(f"Error: {e}")

    client.close()

run_client()




#imports
import socket
import cv2
import pickle
import struct
import numpy as np

#constants
HOST_IP = "10.1.2.139"
CLIENT_NAME = socket.gethostname()
PORT = 8080
ADDR = (HOST_IP,PORT)
FORMAT = "utf-8"
WIDTH = 640
HEIGHT = 400
PAYLOAD_SIZE = 1024



# sender
def close_sender(client_socket):
    try:
        # Send a termination message to the server
        client_socket.sendto(b'', ADDR)
    except socket.error as err:
        print(f"[ERROR] Failed to send termination message: {err}")
    finally:
        # Close the socket
        client_socket.close()


# client
def run_sender():
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"[CLIENT]\nHOST IP:{HOST_IP}\n\n")

    print(f"[CAMERA] Turning on Camera...", end=' ') 
    cam = cv2.VideoCapture("shravan.mp4")
    

    try:
        while cam.isOpened():
            ret,photo = cam.read()
            cv2.imshow('sender',photo)
            ret, buffer= cv2.imencode(".jpg",photo,[int(cv2.IMWRITE_JPEG_QUALITY),30])
            x_bytes = pickle.dumps(buffer)
            sender.sendto(x_bytes,ADDR)
            if cv2.waitKey(10) == 13:
                break
            pass

    finally:
        # Release the camera and destroy all windows here
        cam.release()
        cv2.destroyAllWindows()

    close_sender(sender)

run_sender()


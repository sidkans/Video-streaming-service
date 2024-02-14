#imports
import socket
import cv2
import pickle


#constants
HOST_IP = "192.168.252.240"
PORT = 8080
ADDR = (HOST_IP,PORT)
FORMAT = "utf-8"


#client

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if cam.isOpened():
        try:
            while True:
                ret, frame = cam.read()
                if ret:
                    cv2.imshow('my frame', frame)
                    key = cv2.waitKey(1) &  0xFF
                    if key == ord('q') or key == 27:
                        cam.release()
                        cv2.destroyAllWindows()
                   
        finally:
            # Release the camera and destroy all windows here
            # cam.release()
            # cv2.destroyAllWindows()
            pass

    client.close()

run_client()



run_client()
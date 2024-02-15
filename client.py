#imports
import socket
import cv2
import pickle


#constants
HOST_IP = "10.1.19.15"
PORT = 8080
ADDR = (HOST_IP,PORT)
FORMAT = "utf-8"


#client

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cam = cv2.VideoCapture("./video1.mp4")
    if cam.isOpened():
        try:
            while True:
                ret, frame = cam.read()
                if ret:
                    
                    data = pickle.dumps(frame)
                    client.sendto(data, (HOST_IP, PORT))

                    cv2.imshow('my frame', frame)
                    key = cv2.waitKey(1) &  0xFF
                    if key == ord('q') or key == 27:
                        cam.release()
                        cv2.destroyAllWindows()
                        break
        finally:
            pass

    client.close()

run_client()

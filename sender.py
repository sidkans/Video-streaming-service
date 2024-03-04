#imports
import socket
import cv2
import pickle
import time

#constants
HOST_IP = socket.gethostbyname(socket.gethostname())
ip = HOST_IP.split(".")
HOST_IP_LIST = []
for i in range(5):
    num= int(input("Enter last 3 digits of ip address:"))
    HOST_IP_LIST.append(""+ip[0]+"."+ip[1]+"."+ip[2]+"."+str(num))
print(HOST_IP_LIST)
CLIENT_NAME = socket.gethostname()
PORT = 8080
ADDR = (HOST_IP,PORT)
FORMAT = "utf-8"
WIDTH = 640
HEIGHT = 400
PAYLOAD_SIZE = 1024

# sender
def run_sender():
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # print(f"[CLIENT]\nHOST IP:{HOST_IP}\n\n")

    print(f"[CAMERA] Turning on Camera...") 
    # cam = cv2.VideoCapture("shravan.mp4")
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    

    try:
        while cam.isOpened():
            ret,photo = cam.read()
            cv2.imshow('sender',photo)
            ret, buffer= cv2.imencode(".jpg",photo,[int(cv2.IMWRITE_JPEG_QUALITY),30])
            x_bytes = pickle.dumps(buffer)
            for i in range(5):
                sender.sendto(x_bytes,(HOST_IP_LIST[i],PORT))
            if cv2.waitKey(10) == 13:
                print("[END] Stream is closing...")
                time.sleep(2)
                break
            pass

    finally:
        # Release the camera and destroy all windows here
        
        cam.release()
        cv2.destroyAllWindows()
        print("[TERMINATING] Sender is closing ")
        time.sleep(1.5)

    sender.close()

run_sender()

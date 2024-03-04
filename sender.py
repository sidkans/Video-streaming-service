#imports
import socket
import cv2
import pickle
import time

#constants
HOST_IP = socket.gethostbyname(socket.gethostname())
ip = HOST_IP.split(".")
RECV_IP_LIST = []
while True:
    num= int(input("Enter last 3 digits of ip address (-1 to exit):"))
    if num == -1:
        break
    RECV_IP_LIST.append(""+ip[0]+"."+ip[1]+"."+ip[2]+"."+str(num))

# print(RECV_IP_LIST)
    
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

    if len(RECV_IP_LIST) > 0:

        print(f"[CAMERA] Turning on Camera...") 
        cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        
        
        try:
            while cam.isOpened():
                ret,photo = cam.read()
                cv2.imshow('sender',photo)
                ret, buffer= cv2.imencode(".jpg",photo,[int(cv2.IMWRITE_JPEG_QUALITY),30])
                x_bytes = pickle.dumps(buffer)
                for i in range(5):
                    sender.sendto(x_bytes,(RECV_IP_LIST[i],PORT))
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

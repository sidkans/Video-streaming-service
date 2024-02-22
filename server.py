#imports
import socket
import cv2
import pickle
import time

#constants
HOST = socket.gethostname()
HOST_IP = socket.gethostbyname(HOST)
PORT = 8080
ADDR = (HOST_IP,PORT)
FORMAT = "utf-8"
PAYLOAD_SIZE = 2048


#server
def start_server():
    
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    print(f"[SERVER]\nHOST:{HOST}\nHOST IP:{HOST_IP}\n\n")
    
    try:
        # server.bind(ADDR)
        print("[BIND] Success!\n")
    except socket.error as err:
        print(str(err))
        return
    
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    try:
        while cam.isOpened():
            ret,photo = cam.read()
            cv2.imshow('SERVER',photo)
            ret, buffer= cv2.imencode(".jpg",photo,[int(cv2.IMWRITE_JPEG_QUALITY),30])
            x_bytes = pickle.dumps(buffer)
            server.sendto(x_bytes,ADDR)
            if cv2.waitKey(10) == 13:
                print("[STREAM] Stream is ending ...")
                time.sleep(2)
                break
    
    except Warning:
        pass

    finally:
        # Release the camera and destroy all windows 
        cam.release()
        cv2.destroyAllWindows()
        print(f"[TERMINATING] SERVER IS CLOSING !")
        time.sleep(1)

    server.close()

start_server()
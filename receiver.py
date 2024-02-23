#imports
import socket
import cv2
import pickle
import time
import struct

#constants
HOST = socket.gethostname()
HOST_IP = "192.168.252.240"
PORT = 8080
ADDR = (HOST_IP,PORT)
FORMAT = "utf-8"
PAYLOAD_SIZE = 2048


#receive
def run_receiver():
    receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    print(f"[SERVER]\nHOST:{HOST}\nHOST IP:{HOST_IP}\n\n")
    
    try:
        receiver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,  1)
        receiver.bind(ADDR)
        print("[BIND] Success!\n")
    except socket.error as err:
        print(str(err))
        return
    
    print("[WAITING] Waiting for New Connections ...\n")
    print(f"[LISTENING] on PORT NO:{PORT}\n")

    while True:
        x = receiver.recvfrom(65507)
        try:
            if not x:
                break
            data = x[0]
            data = pickle.loads(data)
            data = cv2.imdecode(data,cv2.IMREAD_COLOR)
            cv2.imshow(f'{HOST}',data)
            if cv2.waitKey(10) == 13:
                cv2.destroyAllWindows()
                break
                
                
        except:
            pass

run_receiver()
#12
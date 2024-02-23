#imports
import socket
import cv2
import pickle
import time

#constants
HOST_IP = ["192.168.252.84","192.168.252.240"]
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
        client_socket.sendall(b'', ADDR)
    except socket.error as err:
        print(f"[ERROR] Failed to send termination message: {err}")
    finally:
        # Close the socket
        client_socket.close()


# client
def run_sender():
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"[CLIENT]\nHOST IP:{HOST_IP}\n\n")

    print(f"[CAMERA] Turning on Camera...") 
    # cam = cv2.VideoCapture("shravan.mp4")
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    

    try:
        while cam.isOpened():
            ret,photo = cam.read()
            cv2.imshow('sender',photo)
            ret, buffer= cv2.imencode(".jpg",photo,[int(cv2.IMWRITE_JPEG_QUALITY),30])
            x_bytes = pickle.dumps(buffer)
            for i in range(2):
                sender.sendto(x_bytes,(HOST_IP[i],PORT))
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

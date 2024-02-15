#imports
import socket
import cv2
import pickle
import struct
import numpy as np

#constants
HOST_IP = "192.168.252.240"
CLIENT_NAME = socket.gethostname()
PORT = 8080
ADDR = (HOST_IP,PORT)
FORMAT = "utf-8"
WIDTH = 640
HEIGHT = 400
PAYLOAD_SIZE = 1024

#client
def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"[SERVER]\nHOST IP:{HOST_IP}\n\n")
    
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # cam = cv2.VideoCapture("./JigsAcademyTesting.mp4")
    print(f"[CAMERA] Turning on Camera...",end= ' ')

    if cam.isOpened():
        print("SUCCESS!")
        try:
            while True:
                ret, frame = cam.read()
                if ret:
                    cv2.imshow(f'{CLIENT_NAME}', frame)
                    frame = cv2.resize(frame,(WIDTH,HEIGHT))
                    key = cv2.waitKey(1) &  0xFF
                    if key == ord('Q') or key == 27:
                        break

                    #serialization of frames first
                    serialized_frames = pickle.dumps(frame)
                    frame_size = len(serialized_frames)
                    packet_count = int(np.ceil(frame_size/PAYLOAD_SIZE))

                    for i in range(packet_count):
                        start = i*PAYLOAD_SIZE
                        end = min((i+1)*PAYLOAD_SIZE,frame_size)
                        packet = serialized_frames[start:end]
                        packet_encoded = struct.pack('!L',i)+packet
                        client.sendto(packet_encoded,ADDR)
                    print("Sending frames") #success!!!!
        finally:
            # Release the camera and destroy all windows here
            cam.release()
            cv2.destroyAllWindows()
            

    client.close()

run_client()

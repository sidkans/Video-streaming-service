#imports
import socket
import cv2
import pickle
import struct
import numpy as np

#constants
HOST_IP = "10.1.1.151"
CLIENT_NAME = socket.gethostname()
PORT = 8080
ADDR = (HOST_IP,PORT)
FORMAT = "utf-8"
WIDTH = 640
HEIGHT = 400
PAYLOAD_SIZE = 1024



# Client
def close_client_socket(client_socket):
    try:
        # Send a termination message to the server
        client_socket.sendto(b'', ADDR)
    except socket.error as err:
        print(f"[ERROR] Failed to send termination message: {err}")
    finally:
        # Close the socket
        client_socket.close()


# client
def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"[CLIENT]\nHOST IP:{HOST_IP}\n\n")

    print(f"[CAMERA] Turning on Camera...", end=' ') 
    cam = cv2.VideoCapture(0)
    

    try:
        '''
        # while cam.isOpened():
        #     # print("SUCCESS!")
        #     ret, frame = cam.read()
        #     if not ret:
        #         break
            
        #     cv2.imshow(f'{CLIENT_NAME}', frame)
        #     frame = cv2.resize(frame, (WIDTH, HEIGHT))
        #     key = cv2.waitKey(20) & 0xFF
        #     if key == ord('Q') or key == 27:
        #         break

        #     # Serialization of frames first
        #     serialized_frames = pickle.dumps(frame)
        #     frame_size = len(serialized_frames)
        #     packet_count = int(np.ceil(frame_size / PAYLOAD_SIZE))

        #     for i in range(packet_count):
        #         start = i * PAYLOAD_SIZE
        #         end = min((i + 1) * PAYLOAD_SIZE, frame_size)
        #         packet = serialized_frames[start:end]
        #         packet_encoded = struct.pack('!L', i) + packet
        #         client.sendto(packet_encoded, ADDR)
        #         # print("Sending frames")  # success!!!!'''
        while cam.isOpened():
            ret,photo = cam.read()
            cv2.imshow('name',photo)
            ret, buffer= cv2.imencode(".jpg",photo,[int(cv2.IMWRITE_JPEG_QUALITY),30])
            x_bytes = pickle.dumps(buffer)
            client.sendto(x_bytes,ADDR)
            if cv2.waitKey(10) == 13:
                break
            pass

    finally:
        # Release the camera and destroy all windows here
        cam.release()
        cv2.destroyAllWindows()

    close_client_socket(client)

run_client()


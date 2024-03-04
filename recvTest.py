import socket
import cv2
import pickle
import struct

# Constants
MULTICAST_GROUP = '239.255.0.1'  # Use the same multicast group address as the sender
MULTICAST_PORT =   8080

def run_receiver():
    # Create a UDP socket
    receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Allow multiple sockets to use the same PORT number
    receiver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,   1)
    
    # Bind the socket to the wildcard address and the multicast port
    receiver.bind(('0.0.0.0', MULTICAST_PORT))
    
    # Tell the operating system to add the socket to the multicast group
    # on all interfaces
    group = socket.inet_aton(MULTICAST_GROUP)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    receiver.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    
    print(f"[RECEIVER] Listening on {MULTICAST_GROUP}:{MULTICAST_PORT}")
    
    while True:
        try:
            data, addr = receiver.recvfrom(65507)
            data = pickle.loads(data)
            frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
            cv2.imshow('receiver', frame)
            if cv2.waitKey(10) ==   13:  # Press 'Enter' to exit
                break
        except (pickle.UnpicklingError, cv2.error) as e:
            print(f"Error receiving data: {e}")
            continue

    cv2.destroyAllWindows()

run_receiver()
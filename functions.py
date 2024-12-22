import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import socket
from deepface import DeepFace
import cv2

def bluetooth_connection(esp32_mac_address: str = "78:E3:6D:18:EF:CE", port: int = 1):
        sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        sock.connect((esp32_mac_address, port))
        return sock

def face_recognition(f1: str, f2: str):
    result = DeepFace.verify(f1, f2)
    match = result['verified']
    print(f"Match: {match}")
    return match

def take_pic():
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Error: Could not access the camera.")
        return None

    print("Press 's' to take a picture and save it, or 'q' to quit.")

    file_name = None
    while True:
        ret, frame = cam.read()
        cv2.imshow('Camera - Press s to save', frame)

        key = cv2.waitKey(1)
        if key & 0xFF == ord('s'):
            file_name = "C:\\Users\\Manav\\Desktop\\Faces\\face_picture.jpg"
            cv2.imwrite(file_name, frame)
            break
        elif key & 0xFF == ord('q'):
            print("Exiting without saving.")
            break

    #Release the webcam and close the window
    cam.release()
    cv2.destroyAllWindows()

    return file_name
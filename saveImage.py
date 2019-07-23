#!/usr/bin/env python3

import socket
import base64
import face_recognition
import sys
#import numpy as np

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65431        # Port to listen on (non-privileged ports are > 1023)


obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]


bush_image = face_recognition.load_image_file("bush.jpg")
bush_face_encoding = face_recognition.face_encodings(bush_image)[0]


known_face_encodings = [

    obama_face_encoding,
    bush_face_encoding
]

known_face_names = [
    "Barack Obama",
    "George Bush"
]


face_encodings = []
face_names = []


while True:
    try:
        #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #    s.bind((HOST, PORT))
        #    s.listen()
        #    conn, addr = s.accept()
        #    with conn:
        #        print('Connected by', addr)
        #        while True:
        #            img_data = conn.recv(8000)
        #            if not img_data:
        #                break
        #            #conn.sendall(img_data)
        #            conn.close()
        #            with open("imageToSave.jpg", "wb") as fh:
        #                fh.write(base64.decodebytes(img_data))
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            print("You uploaded an image of: ", name)
        else:
            print("You uploaded and unrecognizable image!")

        s.close()
    except KeyboardInterrupt:
        print("Goodbye!")
        sys.exit()








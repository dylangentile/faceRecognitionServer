import socket
import pickle
import face_recognition
import wget
import os
import cv2



data = pickle.loads(open("encodings.pickle", "rb").read())
faceNames = data["names"]


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', 25575))
serversocket.listen(1)

connectiontoclient, address = serversocket.accept()
request = b''
request += connectiontoclient.recv(2048)
link = request.decode('utf-8')
#link = 'https://amp.businessinsider.com/images/587fd433ee14b61c008b8b68-750-563.jpg'
#connectiontoclient.send(response)

#print(link, "\n\n")
filename = wget.download(link);

#toleranceStr = input('enter the tolerance: ')
unknown_image = face_recognition.load_image_file(filename)
tolerance = 0.6 #float(toleranceStr)
# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
try:
	unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError:
	connectiontoclient.send(b"failed")
	connectiontoclient.close()
	serversocket.close()







# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
results = face_recognition.compare_faces(data["encodings"], unknown_face_encoding, tolerance)
if True in results:
	x = -1;
	for(i, result) in enumerate(results):
		if result:
			x = i

	connectiontoclient.send(bytes(faceNames[x], 'ascii'))
else:
	connectiontoclient.send(b"failed")



os.remove(filename)
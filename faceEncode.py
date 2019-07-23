from imutils import paths
import face_recognition
import pickle
import os
import cv2

imagePaths = list(paths.list_images("faces"))

knownEncodings = []
knownNames = []


for(i, imagePath) in enumerate(imagePaths):
	print("[INFO] processing image {}/{}".format(i + 1,
		len(imagePaths)))
	name = imagePath.split(os.path.sep)[-2]

	image = cv2.imread(imagePath)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


	encodings = face_recognition.face_encodings(rgb);

	for encoding in encodings:
		knownEncodings.append(encoding)
		knownNames.append(name)


data = {"encodings": knownEncodings, "names": knownNames}
f = open("encodings.pickle", "wb")
f.write(pickle.dumps(data))
f.close()
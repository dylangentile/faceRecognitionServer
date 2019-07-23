import base64 
image = open('bus2.jpg', 'rb') 
image_read = image.read() 
image_64_encode = base64.encodestring(image_read)

print(image_64_encode)
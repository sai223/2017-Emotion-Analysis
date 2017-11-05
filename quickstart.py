import sys
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Making a current path
current_path = os.path.join(os.path.dirname(__file__), sys.argv[1])

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(os.path.dirname(__file__), 'test2.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response_label    = client.label_detection(image=image)
response_property = client.image_properties(image=image)
response_face     = client.face_detection(image=image)

labels = response_label.label_annotations
colors_set = response_property.image_properties_annotation.dominant_colors.colors
faces = response_face.face_annotations


#print(response);
print(response_property);
print(response_face)


print('Labels:')
for label in labels:
    print(label.description)
    print(label.score)

for colors in colors_set:
	print(colors)
'''
for face in faces:
	print(face.detection_confidence)
	print(face.joy_likelihood)
	print(face.sorrow_likelihood)
	print(face.anger_likelihood)
	print(face.surprise_likelihood)
	print(face.under_exposed_likelihood)
	print(face.headwear_likelihood)
'''
print(current_path)
if os.path.exists(current_path):
	print('file exists')


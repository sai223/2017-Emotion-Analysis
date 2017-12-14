import sys
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Making a current path
directory_path = os.path.join(os.path.dirname(__file__), sys.argv[1])

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="../InstagramAnalysis-14a2f6d82abc.json"

# Instantiates a client
client = vision.ImageAnnotatorClient()

file_list = os.listdir(directory_path)
image_num = len(file_list)
# The name of the image file to annotate
  
count = 0

for file in file_list:
	ext = os.path.splitext(file)[-1]
	if ext == '.jpg':
		file_name = os.path.join(directory_path, file)
	else:
		continue
		#count += 1

	count += 1
   	print('done : ' + str(count).rjust(5) + '/' + str(image_num) + ' : ' + str(file))

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

	with open("label.txt", "a") as f:
		for label in labels:
			data_list = []
			data_list.append(file)
			data_list.append('$')
			data_list.append(label.description)
			data_list.append('$')
			data_list.append(str(label.score))
			data_list.append('\n')

			data = ''.join(data_list).encode('utf-8')
			f.write(data)

  	with open("color.txt", "a") as f:
  		for colors in colors_set: 
  			data_list = []
  			data_list.append(file)
			data_list.append('$')
  			data_list.append(str(colors.color.red))
  			data_list.append('$')
  			data_list.append(str(colors.color.green))
  			data_list.append('$')
  			data_list.append(str(colors.color.blue))
  			data_list.append('$')
  			data_list.append(str(colors.score))
  			data_list.append('$')
  			data_list.append(str(colors.pixel_fraction))
  			data_list.append('\n')

  			data = ''.join(data_list).encode('utf-8')
			f.write(data)
    		
   	with open("face.txt", "adirname") as f:
   		for face in faces:
   			data_list = []
   			data_list.append(file)
   			data_list.append('$')
   			data_list.append(str(face.detection_confidence))
   			data_list.append('$')
   			data_list.append(str(face.joy_likelihood))
   			data_list.append('$')
   			data_list.append(str(face.sorrow_likelihood))
   			data_list.append('$')
   			data_list.append(str(face.anger_likelihood))
   			data_list.append('$')
   			data_list.append(str(face.surprise_likelihood))
   			data_list.append('$')
   			data_list.append(str(face.under_exposed_likelihood))
   			data_list.append('$')
   			data_list.append(str(face.blurred_likelihood))
   			data_list.append('\n')

   			data = ''.join(data_list).encode('utf-8')
   			f.write(data)
   			




#print(response);
#print(response_property)
#print(response_face)

'''
print('Labels:')
for label in labels:
    print(label.description)
    print(label.score)

for colors in colors_set:
	print(colors.color)
	
for face in faces:
	print(face.detection_confidence)
	print(face.joy_likelihood)
	print(face.sorrow_likelihood)
	print(face.anger_likelihood)
	print(face.surprise_likelihood)
	print(face.under_exposed_likelihood)
	print(face.headwear_likelihood)

if os.path.exists(directory_path):
	print('file exists')

for file in file_list:
	ext = os.path.splitext(file)[-1]
	if ext == '.jpg':
		print(file)
	else:
		print('This was not IMAGE FILE')
'''
#print(file_name)
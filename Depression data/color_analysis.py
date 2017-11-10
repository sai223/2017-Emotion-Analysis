import os
import sys

DEFAULT = 256
DB = [[0]*(DEFAULT * 3 + 1) for i in range(20000)]


depression_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
happy_path = os.path.join(os.path.dirname(__file__), sys.argv[2])
new_file_name = str(DEFAULT) + ".txt"

past_image_id = ''
image_num = 0
line_num = 0;

#Reading raw data from depression_path(usually depression_color.txt)
with open(depression_path, "r") as f:
	while True:
		line = f.readline()
		if not line: break

		item = line.split('$')

		#Get the value of R, G, B each 
		image_id = item[0]
		red = int(round(float(item[1])))
		green = int(round(float(item[2])))
		blue = int(round(float(item[3])))
		weight = float()

		#Check if image is changed
		if(image_id != past_image_id):
			image_num += 1

		#Count how many the specific R,G,B value exist in one image
		DB[image_num - 1][red] += 1
		DB[image_num - 1][DEFAULT + green] += 1
		DB[image_num - 1][DEFAULT*2 + blue] += 1
		DB[image_num - 1][DEFAULT*3] = 0			

		past_image_id = image_id

		print(str(line_num) + ' done')
		line_num += 1

#Reading raw data from happy_path(usually happy_color.txt)
with open(happy_path, "r") as f:
	while True:
		line = f.readline()
		if not line: break

		item = line.split('$')

		image_id = item[0]
		red = int(round(float(item[1])))
		green = int(round(float(item[2])))
		blue = int(round(float(item[3])))

		if(image_id != past_image_id):
			image_num += 1

		DB[image_num - 1][red] += 1
		DB[image_num - 1][DEFAULT + green] += 1
		DB[image_num - 1][DEFAULT*2 + blue] += 1
		DB[image_num - 1][DEFAULT*3] = 1			

		past_image_id = image_id

		print(str(line_num) + ' done')
		line_num += 1	

#Change data into String
for i in range(image_num):
	for j in range(DEFAULT * 3 + 1):
		DB[i][j] = str(DB[i][j])

#Save data in number
with open(new_file_name, "w") as f:
	for i in range(image_num):
		line = ",".join(DB[i])
		line = line + '\n'
		f.write(line)

print("total " + str(line_num) + " complete")


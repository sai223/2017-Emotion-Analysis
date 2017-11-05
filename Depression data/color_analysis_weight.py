import os
import sys

DEFAULT = 256
DB = [[0]*(DEFAULT * 3 + 1) for i in range(20000)]


depression_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
happy_path = os.path.join(os.path.dirname(__file__), sys.argv[2])
new_file_name = str(DEFAULT) + "_weight" + ".txt"

past_image_id = ''
image_num = 0
line_num = 0;

with open(depression_path, "r") as f:
	while True:
		line = f.readline()
		if not line: break

		item = line.split('$')

		image_id = item[0]
		red = int(round(float(item[1])))
		green = int(round(float(item[2])))
		blue = int(round(float(item[3])))
		weight = float(item[4])

		if(image_id != past_image_id):
			image_num += 1

		#DB[image_num - 1][0] = image_id
		DB[image_num - 1][red] += round(weight, 3)
		DB[image_num - 1][DEFAULT + green] += round(weight, 3)
		DB[image_num - 1][DEFAULT*2 + blue] += round(weight, 3)
		DB[image_num - 1][DEFAULT*3] = 0				

		past_image_id = image_id

		print(str(line_num) + ' done')
		line_num += 1

with open(happy_path, "r") as f:
	while True:
		line = f.readline()
		if not line: break

		item = line.split('$')

		image_id = item[0]
		red = int(round(float(item[1])))
		green = int(round(float(item[2])))
		blue = int(round(float(item[3])))
		weight = float(item[4])

		if(image_id != past_image_id):
			image_num += 1

		#DB[image_num - 1][0] = image_id
		DB[image_num - 1][red] += round(weight, 3)
		DB[image_num - 1][DEFAULT + green] += round(weight, 3)
		DB[image_num - 1][DEFAULT*2 + blue] += round(weight, 3)
		DB[image_num - 1][DEFAULT*3] = 1			

		past_image_id = image_id

		print(str(line_num) + ' done')
		line_num += 1	

for i in range(image_num):
	for j in range(DEFAULT * 3 + 1):
		DB[i][j] = str(DB[i][j])

with open(new_file_name, "w") as f:
	for i in range(image_num):
		line = ",".join(DB[i])
		line = line + '\n'
		f.write(line)

print("total " + str(line_num) + " complete")


import os
import sys

DEFAULT = 26
DB = [[0]*(DEFAULT * 3 + 1) for i in range(10000)]

directory_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
new_file_name = "analysis_" + directory_path

past_image_id = ''
image_num = 0
line_num = 0;

with open(directory_path, "r") as f:
	while True:
		line = f.readline()
		if not line: break

		item = line.split('$')

		image_id = item[0]
		red = int(round(float(item[1]))) / 10
		green = int(round(float(item[2]))) / 10
		blue = int(round(float(item[3]))) / 10

		if(image_id != past_image_id):
			image_num += 1

		DB[image_num - 1][1 + red] += 1
		DB[image_num - 1][1 + DEFAULT + green] += 1
		DB[image_num - 1][1 + DEFAULT*2 + blue] += 1			

		past_image_id = image_id

		print(line)
		print(str(line_num) + ' done')
		line_num += 1

with open(new_file_name, "w") as f:
	for i in range(image_num):
		line = "$".join(DB[i])
		line.append('\n')
		f.write(line)


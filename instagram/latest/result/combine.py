
DB = [[] for i in range(983)]
color_DB = [[] for i in range(983)]
label_DB = [[] for i in range(983)]

line_num = 0;
with open('color_test_result.txt', 'r') as f:
	while True:
		line = f.readline()
		if not line: break

		line1 = " ".join(line.split())
		item = line1.split(' ')

		for i in range(len(item)):
			color_DB[line_num].append(item[i])

		line_num += 1	

print("color read done : " + str(line_num))
print(color_DB[0])

line_num = 0;
with open('label_test_result.txt', 'r') as f:
	while True:
		line = f.readline()
		if not line: break

		line1 = " ".join(line.split())
		item = line1.split(' ')

		for i in range(len(item)):
			label_DB[line_num].append(item[i])

		line_num += 1

print("label read done : " + str(line_num))
print(label_DB)

for i in range(len(color_DB)):
	for j in range(len(label_DB)):
		if(color_DB[i][0] == label_DB[j][0]):
			DB[i].append(color_DB[i][0])
			DB[i].append(color_DB[i][1])
			DB[i].append(label_DB[j][1])

			DB[i].append(color_DB[i][2])
			DB[i].append(label_DB[j][2])

			break;

with open('combine.txt', 'w') as f:
	for i in range(len(DB)):
		line = " ".join(DB[i])
		line = line + '\n'

		f.write(line)





import os
import sys


from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import train_test_split

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import confusion_matrix
import pickle 


import numpy as np

DB = [[] for i in range(20000)]

latest_label_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
new_file_name = "latest_label_data" + ".txt"

past_image_id = ''
image_num = 0
line_num = 0;

#Reading raw data from depression_path(usually depression_color.txt)
with open(latest_label_path, "r") as f:
	while True:
		line = f.readline()
		if not line: break

		item = line.split('$')

		#Get the value of R, G, B each 
		image_id = item[0] 
		object_name = item[1] 
		score = float(item[2])

		#Check if image is changed
		if(image_id != past_image_id):
			DB[image_num].append(image_id)
			DB[image_num].append(image_num)
			image_num += 1

		#Count how many the specific R,G,B value exist in one 
		if(score >= 0.8):
			DB[image_num - 1].append(object_name)

		past_image_id = image_id

		print(str(line_num) + ' done')
		line_num += 1

print("total line : " + str(line_num) + " complete")
print("total image: " + str(image_num) + " complete")

for i in range(image_num):
	for j in range(len(DB[i])):
		DB[i][j] = str(DB[i][j])

for i in range(image_num):
	line = " ".join(DB[i])
		
	item = line.split(" ")
	DB[i] = []
	for j in range(len(item)):
		DB[i].append(item[j])

'''
for i in range(len(DB[:468])):
	print(DB[i])
'''

DB_X = []
DB_X_label = []

NONE = []
NONE_Y = []


for i in range(len(DB[:467])):
	if len(DB[i]) == 2:
		NONE.append(DB[i])

	else:
		line = ' '.join(DB[i][2:])
		DB_X.append(line)
		DB_X_label.append(DB[i][0:2])
'''
for i in range(len(DB_X)):
	print(DB_X_label[i] + DB_X[i])
for i in range(len(NONE)):
	print(NONE[i]);
'''

print(len(DB_X))
print(len(NONE))


def CounterVector():

	label_model = pickle.load(open('label_CounterVector.pkl', 'rb'))
	label_vect = pickle.load(open('label_vect.pkl', 'rb'))

	X_test = label_vect.transform(DB_X)

	feature_names = label_vect.get_feature_names()

	print(format(repr(X_test)))

	Y_pred = label_model.predict(X_test)
	Y_prob = label_model.predict_proba(X_test)


	print(len(DB_X))
	for i in range(len(DB_X_label)):
		print(DB_X_label[i])



	with open("classify_with_label_result.txt", "w") as f:
		for i in range(image_num):
			line = ''
			for j in range(len(DB_X)):
				if(str(i) == DB_X_label[j][1]):
					print('check1')
					line = str(DB_X_label[j][0]) + ' ' + str(Y_pred[j]) + ' ' + str(round(float(np.max(Y_prob[j])), 3)) + '\n'
					break
			for k in range(len(NONE)):
				if(str(i) == NONE[k][1]):
					print('check2')
					line = str(NONE[k][0]) + '\n'
					break

			f.write(line)

if __name__ == '__main__':
	CounterVector();

'''
	with open("label_test_result.txt", "w") as f:
		for i in range(len(DB_X)):
			line = str(DB_label[i]) + ' ' + str(Y_pred[i]) + ' ' + str(round(float(np.max(Y_prob[i])), 3))
			line = line + '\n'
			f.write(line)

		for j in range(len(NONE_label)):
			line = str(DB_label[j]) + ' ' + str(3) + ' ' + str(3)
			line = line + '\n'
			f.write(line)

'''





'''

for i in range(image_num):
	for j in range(len(DB[i])):
		DB[i][j] = str(DB[i][j])

with open(new_file_name, "w") as f:
	for i in range(image_num):
		line = ",".join(DB[i])
		if(line == "0"):
			continue
			
		line = line + '\n'
		f.write(line)
		'''





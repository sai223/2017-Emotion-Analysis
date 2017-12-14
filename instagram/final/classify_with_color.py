import os
import sys
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np
from time import time
import pickle

color_model = pickle.load(open('color_SVM.pkl', 'rb'))


#Work can be done in '26' or '256 by assigning them in DEFAULT
DEFAULT = 26
DB = [[0]*(DEFAULT * 3 + 1) for i in range(20000)]

#Getting the path of depression_data(usually depression_color.txt) and happy_data(usually happy_color.txt)
latest_color_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
#happy_path = os.path.join(os.path.dirname(__file__), sys.argv[2])
new_file_name = "latest_color_data" + ".txt"

past_image_id = ''
image_num = 0
line_num = 0;

#Reading raw data from depression_path(usually depression_color.txt)
with open(latest_color_path, "r") as f:
	while True:
		line = f.readline()
		if not line: break

		item = line.split('$')

		#Get the value of R, G, B each 
		image_id = item[0]
		red = int(round(float(item[1]))) / 10
		green = int(round(float(item[2]))) / 10
		blue = int(round(float(item[3]))) / 10

		#weight is the score of color above
		weight = float(item[4])

		#Check if image is changed
		if(image_id != past_image_id):
			image_num += 1

		#Count how many the specific R,G,B value exist in one image(using weight)
		DB[image_num - 1][0] = image_id
		DB[image_num - 1][1 + red] += round(weight, 3)
		DB[image_num - 1][1 + DEFAULT + green] += round(weight, 3)
		DB[image_num - 1][1 + DEFAULT*2 + blue] += round(weight, 3)			

		past_image_id = image_id

		print(str(line_num) + ' done')
		line_num += 1

print("total line : " + str(line_num) + " complete")
print("total image: " + str(image_num) + " complete")

if __name__ == '__main__':

	DBnp = np.array(DB)

	X_test = DBnp[:image_num,1:]
	Y_test = DBnp[:image_num,-1]

	print(len(X_test))
	print(X_test)
	print(Y_test)

	sc = StandardScaler()
	sc.fit(X_test)

	X_test_std = sc.transform(X_test)

	Y_pred = color_model.predict(X_test_std)
	Y_prob = color_model.predict_proba(X_test)

	with open("classify_with_color_result.txt", "w") as f:
		for i in range(len(X_test)):
			line = str(DB[i][0]) + ' ' + str(Y_pred[i]) + ' ' + str(round(float(np.max(Y_prob[i])), 3))
			line = line + '\n'
			f.write(line)


	print(Y_pred[0])
	print(X_test[0])
	print(DB[0][0])

	print(Y_pred[5])
	print(X_test[5])
	print(DB[5][0])

	



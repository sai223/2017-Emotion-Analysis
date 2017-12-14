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
import pandas as pd

color_model = pickle.load(open('color_SVM.pkl', 'rb'))

total_line = 0
with open('latest_color_data.txt', "r") as f:
	while True:
		line = f.readline()
		if not line: break
		total_line += 1

DB = [[] for i in range(983)]

line_num = 0;
with open('latest_color_data.txt', "r") as f:
	while True:
		line = f.readline()
		if not line: break

		line1 = " ".join(line.split())
		item = line1.split(',')

		for i in item:
			DB[line_num].append(i)

		line_num += 1

if __name__ == '__main__':

	DBnp = np.array(DB)

	X_test = DBnp[:,1:]
	Y_test = DBnp[:,-1]

	print(len(X_test[0]))
	print(X_test)
	print(Y_test)

	sc = StandardScaler()
	sc.fit(X_test)

	X_test_std = sc.transform(X_test)

	Y_pred = color_model.predict(X_test_std)
	Y_prob = color_model.predict_proba(X_test)

	with open("color_test_result.txt", "w") as f:
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

	print(Y_pred[982])
	print(X_test[982])
	print(DB[982][0])
	








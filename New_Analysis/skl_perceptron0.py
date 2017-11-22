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

DEFAULT = 256

total_line = 0;
with open(str(DEFAULT) + ".txt", "r") as f:
	while True:
		line = f.readline()
		if not line: break;
		total_line += 1

DB = [[0]*(DEFAULT + 1) for i in range(total_line)]

line_num = 0;
with open(str(DEFAULT) + ".txt", "r") as f:
	while True:
		line = f.readline()
		if not line: break

		line1 = " ".join(line.split())
		item = line1.split(',')
		#print(len(item))
		for i in range(len(item)):
			DB[line_num][i] = item[i]
			#print(str(i) + ' : ' + str(DB[line_num][i]))

		line_num += 1

for i in range(line_num):
	for j in range(DEFAULT + 1):
		DB[i][j] = float(DB[i][j])
		#print(str(i) + ' : ' + str(DB[i][i]))

print("#####File Read Complete : " + str(line_num))

if __name__ == '__main__':

	DBnp = np.array(DB)

	X = DBnp[:,:-1]
	Y = DBnp[:,-1]

	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

	sc = StandardScaler()
	sc.fit(X_train)
	X_train_std = sc.transform(X_train)
	X_test_std = sc.transform(X_test)

	f = open(str(DEFAULT) + "_result" + ".txt", "w")

	#Logistic Regression

	f.write('### Rogistic Regression ###\n' )
	C_group = [0.1]
	penalty_group = ['l2']

	for C in C_group:
		for penalty in penalty_group:
			ml = LogisticRegression(C=C, penalty=penalty)
			start_time = time()
			ml.fit(X_train_std, Y_train)
			end_time = time()
			print(str(end_time - start_time))

			Y_pred = ml.predict(X_test_std)

			f.write('C = ' + str(C) + ' penalty = ' + penalty)
			f.write('TEST NUM : %d, ERROR NUM : %d, ACCURACY : %.2f' %(len(Y_test), (Y_test != Y_pred).sum(), accuracy_score(Y_test, Y_pred)))
			f.write('\n')

	print("#####Rogistic Regression Complete / \n")

	#Random Forest

	f.write('### Random Forest ###\n' )
	n_estimators_group = [300]

	for n_estimators in n_estimators_group:
		ml = RandomForestClassifier(criterion='entropy', n_estimators=n_estimators, n_jobs=2, random_state=1)
		start_time = time()
		ml.fit(X_train_std, Y_train)
		end_time = time()
		print(str(end_time - start_time))

		Y_pred = ml.predict(X_test_std)

		f.write('n_estimators = ' + str(n_estimators))
		f.write('TEST NUM : %d, ERROR NUM : %d, ACCURACY : %.2f' %(len(Y_test), (Y_test != Y_pred).sum(), accuracy_score(Y_test, Y_pred)))
		f.write('\n')

	print("#####Random Forest Complete / \n")

	#SVM

	f.write('### SVM ###\n' )
	C_group = [1]

	for C in C_group:
		ml = SVC(kernel='rbf', C=C, random_state=0)
		start_time = time()
		ml.fit(X_train_std, Y_train)
		end_time = time()
		print(str(end_time - start_time))

		Y_pred = ml.predict(X_test_std)

		f.write('C = ' + str(C))
		f.write('TEST NUM : %d, ERROR NUM : %d, ACCURACY : %.2f' %(len(Y_test), (Y_test != Y_pred).sum(), accuracy_score(Y_test, Y_pred)))
		f.write('\n')

	print("#####SVM Complete / \n")


	f.close()
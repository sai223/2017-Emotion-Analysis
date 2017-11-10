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

DEFAULT = 26

total_line = 0;
with open(str(DEFAULT) + "_weight.txt", "r") as f:
	while True:
		line = f.readline()
		if not line: break;
		total_line += 1

DB = [[0]*(DEFAULT * 3 + 1) for i in range(total_line)]

line_num = 0;
with open(str(DEFAULT) + "_weight.txt", "r") as f:
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
	for j in range(DEFAULT):
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

	f = open(str(DEFAULT) + "_weight_result" + ".txt", "w")

	#Perceptron
	ml = Perceptron(eta0=0.01, n_iter=40, random_state=0)

	start_time = time()
	ml.fit(X_train_std, Y_train)
	end_time = time()

	Y_pred = ml.predict(X_test_std)
	f.write('### Perceptron ###\n')
	f.write('TEST NUM : %d, ERROR NUM : %d, ACCURACY : %.2f' %(len(Y_test), (Y_test != Y_pred).sum(), accuracy_score(Y_test, Y_pred)))
	f.write('\n')
	print("#####Perceptron Complete / " + str(end_time - start_time) + '\n')

	#Logistic Regression

	f.write('### Rogistic Regression ###\n' )
	C_group = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
	penalty_group = ['l1', 'l2']

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

	#Decision Tree

	f.write('### Decision Tree ###\n' )
	max_depth_group = [5, 8, 15, 25, 30]
	criterion_group = ['entropy', 'gini']

	for max_depth in max_depth_group:
		for criterion in criterion_group:
			ml = DecisionTreeClassifier(criterion=criterion, max_depth=max_depth, random_state=0)
			start_time = time()
			ml.fit(X_train_std, Y_train)
			end_time = time()
			print(str(end_time - start_time))

			Y_pred = ml.predict(X_test_std)

			f.write('max_depth = ' + str(max_depth) + ' criterion = ' + criterion)
			f.write('TEST NUM : %d, ERROR NUM : %d, ACCURACY : %.2f' %(len(Y_test), (Y_test != Y_pred).sum(), accuracy_score(Y_test, Y_pred)))
			f.write('\n')

	print("#####Decision Tree Complete / ")

	#Random Forest

	f.write('### Random Forest ###\n' )
	n_estimators_group = [120, 300, 500, 800, 1200]

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
	C_group = [0.001, 0.01, 0.1, 1, 10, 100, 1000]

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
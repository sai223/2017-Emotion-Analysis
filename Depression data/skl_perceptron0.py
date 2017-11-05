from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

DEFAULT = 256

total_line = 0;
with open(str(DEFAULT) + ".txt", "r") as f:
	while True:
		line = f.readline()
		if not line: break;
		total_line += 1

DB = [[0]*(DEFAULT * 3 + 1) for i in range(total_line)]

line_num = 0;
with open(str(DEFAULT) + ".txt", "r") as f:
	while True:
		line = f.readline()
		if not line: break

		print("=========" + str(line_num) + "==================")
		for i in range(len(line) - 1):
			print(i)
			DB[line_num][i] = line[i]

		line_num += 1

for i in range(line_num):
	for j in range(DEFAULT):
		DB[i][j] = int(DB[i][j])

print len(DB[0])

if __name__ == '__main__':

	DBnp = np.array(DB)
	#print(DBnp.dtype)
	X = DBnp[:,:-1]
	Y = DBnp[:,-1]


	print X
	print len(X[0])
	print Y
	print len(Y)
	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

	sc = StandardScaler()
	sc.fit(X_train)
	X_train_std = sc.transform(X_train)
	X_test_std = sc.transform(X_test)

	#ml = Perceptron(eta0=0.01, n_iter=40, random_state=0)
	ml = LogisticRegression(C=100, penalty='l2', tol=0.2)
	print(len(X_train_std), len(Y_train))
	ml.fit(X_train_std, Y_train)
	Y_pred = ml.predict(X_test_std)
	print('TEST NUM : %d, ERROR NUM : %d' %(len(Y_test), (Y_test != Y_pred).sum()))
	print('ACCURACY : %.2f' %accuracy_score(Y_test, Y_pred))

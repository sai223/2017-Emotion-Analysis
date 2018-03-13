
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

'''
total_line = 0;
with open("latest_label_data" + ".txt", "r") as f:
	while True:
		line = f.readline()
		if not line: break;
		total_line += 1

DB = [[] for i in range(total_line)]
DB_X = []
DB_label = []

NONE_label = []
NONE_Y = []

line_num = 0;
with open("latest_label_data" + ".txt", "r") as f:
	while True:
		line = f.readline()
		if not line: break


		line1 = " ".join(line.split())
		item = line1.split(',')

		if len(item) == 1:
			line2 = ' '.join(item[0])
			NONE_label.append(line2)
			line_num += 1

		else:
			line2 = ' '.join(item[1:])
			DB_X.append(line2)
			DB_label.append(item[0])
			line_num += 1


print("#####File Read Complete : " + str(line_num))

label_vect = pickle.load(open('label_vect.pkl', 'rb'))
label_model = pickle.load(open('label_CounterVector.pkl', 'rb'))
'''

'''
#DB_X_train, DB_X_test, Y_train, Y_test = train_test_split(DB_X, DB_Y, test_size=0.3, random_state=0)

#print("DB_X_train : {}".format(len(DB_X_train)))
#print("DB_X_test : {}".format(len(DB_X_test)))
#print("Y_train : {}".format(len(Y_train)))
#print("Y_test : {}".format(len(Y_test)))

'''
def CounterVector():

	label_model = pickle.load(open('label_CounterVector.pkl', 'rb'))
	label_vect = pickle.load(open('label_vect.pkl', 'rb'))



#	X_test = label_vect.transform(DB_X)

	feature_names = label_vect.get_feature_names()

	print("CHECK : \n{}".format(feature_names[:]))

	print(format(repr(X_test)))

	Y_pred = label_model.predict(X_test)
	Y_prob = label_model.predict_proba(X_test)

	print(Y_prob)

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
	print(Y_pred[0])
	print(DB_X[0])
	print(DB_label[0])

	print(Y_pred[5])
	print(DB_X[5])
	print(DB_label[5])

	print(Y_pred[7])
	print(DB_X[7])
	print(DB_label[7])

	for i in range(783):
		print(Y_pred[i])


	print(Y_pred[500])
	print(DB_X[500])
	print(DB_label[500])
'''

'''
	scores = cross_val_score(LogisticRegression(), X_train, Y_train, cv=5)
	print("Counter Vector / Train result : {:.2f}".format(np.mean(scores)))

	param_grid = {'C': [0.001, 0.01, 0.1, 1, 10]}
	grid = GridSearchCV(LogisticRegression(), param_grid, cv=5)
	grid.fit(X_train, Y_train)
	print("Optimal score : {:.2f}".format(grid.best_score_))
	print("Optimal param : ", grid.best_params_)

	X_test = vect.transform(DB_X_test)
	print("Counter Vector / Test Score : {:.2f}".format(grid.score(X_test, Y_test)))
'''

if __name__ == '__main__':
	CounterVector()


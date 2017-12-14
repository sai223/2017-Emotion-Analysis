
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


total_line = 0;
with open("label_analysis_result" + ".txt", "r") as f:
	while True:
		line = f.readline()
		if not line: break;
		total_line += 1

DB = [[] for i in range(total_line)]
DB_X = []
DB_Y = []

line_num = 0;
with open("label_analysis_result" + ".txt", "r") as f:
	while True:
		line = f.readline()
		if not line: break


		line1 = " ".join(line.split())
		item = line1.split(',')

		line2 = ' '.join(item[:-1])

		DB_X.append(line2)
		DB_Y.append(item[-1])
		line_num += 1



print("#####File Read Complete : " + str(line_num))

def CounterVector():
	vect = CountVectorizer(min_df=10);
	vect.fit(DB_X)

	X_train = vect.transform(DB_X)
	print(format(X_train[1]))

	X = [0,1,1,1,1,1,0,0,0,0]

	print(np.vstack((X,X_train[1])).T)


	feature_names = vect.get_feature_names()
	print(format(repr(X_train)))


	logreg = LogisticRegression(C=10)
	scores = cross_val_score(logreg,X_train, DB_Y, cv=10)

	print("LET'S SEE THE RESULT:{}".format(scores))
	print("MEAN: {:.2f}".format(scores.mean()))


if __name__ == '__main__':

	CounterVector()

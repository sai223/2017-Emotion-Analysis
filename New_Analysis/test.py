
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import train_test_split

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV


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


DB_X_train, DB_X_test, Y_train, Y_test = train_test_split(DB_X, DB_Y, test_size=0.3, random_state=0)

print("DB_X_train : {}".format(len(DB_X_train)))
print("DB_X_test : {}".format(len(DB_X_test)))
print("Y_train : {}".format(len(Y_train)))
print("Y_test : {}".format(len(Y_test)))

def CounterVector():
	vect = CountVectorizer();
	vect.fit(DB_X_train)

	X_train = vect.transform(DB_X_train)

	feature_names = vect.get_feature_names()

	scores = cross_val_score(LogisticRegression(), X_train, Y_train, cv=5)
	print("Counter Vector / Train result : {:.2f}".format(np.mean(scores)))

	param_grid = {'C': [0.001, 0.01, 0.1, 1, 10]}
	grid = GridSearchCV(LogisticRegression(), param_grid, cv=5)
	grid.fit(X_train, Y_train)
	print("Optimal score : {:.2f}".format(grid.best_score_))
	print("Optimal param : ", grid.best_params_)

	X_test = vect.transform(DB_X_test)
	print("Counter Vector / Test Score : {:.2f}".format(grid.score(X_test, Y_test)))

def TfIdf():
	pipe = make_pipeline(TfidfVectorizer(min_df=5), LogisticRegression())
	param_grid = {'logisticregression__C': [0.001, 0.01, 0.1, 1, 10]}

	grid = GridSearchCV(pipe, param_grid, cv=5)
	grid.fit(DB_X_train, Y_train)
	print("Tf-idf / Train result : {:.2f}".format(grid.best_score_))
	print("Optimal param : ", grid.best_params_)
	print("Tf-idf / Test Score : {:.2f}".format(grid.score(DB_X_test, Y_test)))

	vectorizer = grid.best_estimator_.named_steps["tfidfvectorizer"]
	X_train = vectorizer.transform(DB_X_train)
	max_value = X_train.max(axis=0).toarray().ravel()
	sorted_by_tfidf = max_value.argsort()

	feature_names = np.array(vectorizer.get_feature_names())

	print("tfidf lowest feature:\n{}".format(feature_names[sorted_by_tfidf[:20]]))
	print("tfidf highest feature:\n{}".format(feature_names[sorted_by_tfidf[-20:]]))

if __name__ == '__main__':


	#print("size : {}".format(len(vect.vocabulary_)))
	#print("word : \n {}".format(vect.vocabulary_))


	'''
	print("feature num: {}".format(len(feature_names)))
	print("first 20: {}".format(feature_names[:20]))
	print("1000 to 1010: {}".format(feature_names[1000:1010]))
	print("every 100: {}".format(feature_names[::100]))
	'''

	CounterVector()
	TfIdf()
	#TF-IDF





	#X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

	#print("y_train: {}".format(np.bincount(y_train)))


	#Y = DBnp[:,-1]
	#print(Y)
	#print("=======================")
	#X = DBnp[:,:-1]
	#print(X)
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

import numpy as np
from time import time
import pickle
import pandas as pd

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

    #X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

    sc = StandardScaler()
    sc.fit(X)
    X_train_std = sc.transform(X)
    #X_test_std = sc.transform(X_test)

    #SVM
    C_group = [1]
    #Gamma_group = [0.1, 1]
    
    best_score = 0
    #for G in Gamma_group:
    for C in C_group:
        ml = SVC(C=C, probability=True)
        scores = cross_val_score(ml, X_train_std, Y, cv=5)
            
        score = np.mean(scores)
                
        print('scores : ' + str(scores))
        print('mean   : ' + str(score))

        print('done')
                
    #svm = SVC(**best_parameters)
    #svm.fit(X)
        
    #mglearn.plots.plot_cross_val_selection()
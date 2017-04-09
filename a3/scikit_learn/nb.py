import sklearn
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_svmlight_file
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

print;
print "---------Implementation of a classifier with Gaussian Naive Bayes---------------"

X, y = load_svmlight_file('a3.libsvm');
print;
print("Total number of instances: %d" %X.shape[0]);
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4, random_state = 0);
print("Num Instances of the training set : %d" % X_train.shape[0]);
print("Num Intances of the testing set : %d" % X_test.shape[0]);
print;
clf = GaussianNB();
X_train = X_train.toarray();  #requested by compiler, since
X_test = X_test.toarray();    #these are 'dense' 
clf.fit(X_train, y_train);    #however, the y's are np.arrays
y_pred = clf.predict(X_test); #so there's no need to fix that.
y_true = y_test; 
c_m = confusion_matrix(y_true, y_pred);
labels = ["blues","jazz","rock"];
categories = ["a","b","c"];
print " a  b  c <-- classified as";
for i in range(3):
	print c_m[i],
	print("| %s = %s" % (categories[i],labels[i]));
scores = cross_val_score(clf, X_test, y_test , cv = 5);
print;
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()*2) );



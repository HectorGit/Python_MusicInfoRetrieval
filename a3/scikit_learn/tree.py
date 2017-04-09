import sklearn
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_svmlight_file
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

X, y = load_svmlight_file('a3.libsvm');

print;
print "---------Implementation of a classifier with DecisionTreeClassifier---------------"
print;
print("Total number of instances: %d" %X.shape[0]);
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4, random_state = 0);
print("Num Instances of the training set : %d" % X_train.shape[0]);
print("Num Intances of the testing set : %d" % X_test.shape[0]);
print;
clf = tree.DecisionTreeClassifier();
clf = clf.fit(X_train, y_train);

y_pred = clf.predict(X_test); #this is a list of 0 = blues, 1 = jazz, and 2 = rock
y_true = y_test; #ground truth
c_m = confusion_matrix(y_true, y_pred);
labels = ["blues","jazz","rock"];
categories = ["a","b","c"];

print " a   b   c  <-- classified as";
for i in range(3):
	print c_m[i],
	print("| %s = %s" % (categories[i],labels[i]));
	
scores = cross_val_score(clf, X_test, y_test , cv = 5);
print;
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()*2) );


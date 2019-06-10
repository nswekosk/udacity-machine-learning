import sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(features_train, labels_train);
pred = clf.predict(features_test)

'''
Define the accuracy of the predictions

2 methods:
- 1: Write code that compares predictions to y_test, element-by-element
- 2: Google "sklearn accuracy" and go from there
'''

from sklearn.metrics import accuracy_score
y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]

accuracy_score(y_true, y_pred)

#!/usr/bin/python

from time import time
from sklearn.tree import DecisionTreeClassifier

def classify(features_train, labels_train, features_test, labels_test):
  clf = DecisionTreeClassifier(min_samples_split=20)

  t0 = time()
  clf.fit(features_train, labels_train)
  print "training time: ", round(time()-t0, 3), " s"

  t0 = time()
  pred = clf.predict(features_test)
  print "prediction time: ", round(time()-t0, 3), " s"

  return clf, pred
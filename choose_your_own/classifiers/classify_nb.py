#!/usr/bin/python

from time import time
from sklearn.naive_bayes import GaussianNB

def classify(features_train, labels_train, features_test, labels_test):
  clf = GaussianNB()
  
  t0 = time()
  clf.fit(features_train, labels_train)
  print "training time: ", round(time()-t0, 3), " s"

  t0 = time()
  pred = clf.predict(features_test)
  print "prediction time: ", round(time()-t0, 3), " s"

  return clf, pred
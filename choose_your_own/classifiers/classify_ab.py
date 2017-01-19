#!/usr/bin/python

from time import time
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC

def classifya(features_train, labels_train, features_test, labels_test):
  c=10000
  gamma=15
  # clf = AdaBoostClassifier(SVC(kernel="rbf", C=c, gamma=gamma), n_estimators=50)
  clf = AdaBoostClassifier(SVC(kernel="rbf", C=c, gamma=gamma), n_estimators=500, algorithm="SAMME")

  t0 = time()
  clf.fit(features_train, labels_train)
  print "training time: ", round(time()-t0, 3), " s"

  t0 = time()
  pred = clf.predict(features_test)
  print "prediction time: ", round(time()-t0, 3), " s"

  return clf, pred
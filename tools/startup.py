#!/usr/bin/python

print
print "checking for nltk"
try:
    import nltk
except ImportError:
    print "you should install nltk before continuing"

print "checking for numpy"
try:
    import numpy
except ImportError:
    print "you should install numpy before continuing"

print "checking for scipy"
try:
    import scipy
except:
    print "you should install scipy before continuing"

print "checking for sklearn"
try:
    import sklearn
except:
    print "you should install sklearn before continuing"

print
print "downloading the Enron dataset (this may take a while)"
print "to check on progress, you can cd up one level, then execute <ls -lthr>"
print "Enron dataset should be last item on the list, along with its current size"
print "download will complete at about 423 MB"
print
import urllib
import os
os.chdir("..")
url = "https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tgz"
targetfile = "enron_mail_20150507.tgz"
if os.path.exists(targetfile) and os.path.isfile(targetfile) and (os.path.getsize(targetfile) == 443254787):
    print "you have the latest enron_mail_20150507.tgz"
else:
    urllib.urlretrieve(url, filename=targetfile) 
    print "download complete!"
    print
    print "unzipping Enron dataset (this may take a while)"
    import tarfile
    tfile = tarfile.open("enron_mail_20150507.tgz", "r:gz")
    tfile.extractall(".")

print
print "you're ready to go!"
import urllib
import os

image = urllib.URLopener()
os.chdir('file')

for i in range(81):
  image.retrieve("http://eli.luberoff.com/set%20cards/" + str(i) + ".JPG", str(i) + ".JPG")
  print "downloaded " + str(i)

from myStore import *
import urllib
import os

os.system("clear")
htmlfile = urllib.urlopen("http://www.sohu.com/a/155964201_114988?_f=index_news_1")
htmltxt = htmlfile.read()
print len(htmltxt)
print htmltxt

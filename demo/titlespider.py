#coding: UTF-8
import urllib
import re

urls = "http://www.nytimes.com/","http://www.crummy.com/software/BeautifulSoup/","http://www.shido.info/py/tkinter3.html"
i = 0
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)

while i < len(urls):
	htmlfile = urllib.urlopen(urls[i])
	htmltext = htmlfile.read()
	titles = re.findall(pattern, htmltext)
	titles =  str(titles).encode('utf-8')
	
	print titles
	i +=1
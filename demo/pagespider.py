#coding: UTF-8
import urllib 

#site names
urls = "http://www.nytimes.com/","http://www.crummy.com/software/BeautifulSoup/#

i = 0

while i < len(urls):
	htmlfile = urllib.urlopen(urls[i])
	htmltext = htmlfile.read()
	print htmltext
	i +=1
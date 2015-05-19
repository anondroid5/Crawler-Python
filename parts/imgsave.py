#coding: UTF-8

import sys, urllib
import os.path

def download(url):
	img = urllib.urlopen(url)
	localfile = open(os.path.basename(url),'wb')
	localfile.write(img.read())
	img.close()
	localfile.close()

#url = "http://なんちゃら.jpg"

URL_LIST = ["http://www.crummy.com/software/BeautifulSoup/10.1.jpg",
		"http://www.crummy.com/nb//resources/img/somerights20.jpg"
	   ]

for urls in URL_LIST:
	download(urls)
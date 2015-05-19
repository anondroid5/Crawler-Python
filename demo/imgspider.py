#coding: UTF-8
import urllib
import re

urls = "http://www.nytimes.com/","http://www.crummy.com/software/BeautifulSoup/"
i = 0
regex_title ='<title>(.+?)</title>'
pattern_title = re.compile(regex_title)
regex_img = '<img .*?src="(.*?)".*?>'
pattern_img = re.compile(regex_img)

while i < len(urls):
	htmlfile = urllib.urlopen(urls[i])
	htmltext = htmlfile.read() # html全体の取得
	
	print '*' *30 +'取得結果' +'*' *30
	#サイト内のtitleタグの取得
	titles = re.findall(pattern_title, htmltext)
	
	print 'サイト名:' + str(titles[0])
	print 'ドメイン名:' + urls[i]
	
	#サイト内のimgタグの取得
	img = re.findall(pattern_img, htmltext)
	for imgs in img:
		print imgs
	i +=1
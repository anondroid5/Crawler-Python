#coding: UTF-8
import math
while True:
	reply = raw_input('Enter text: ')
	if reply == 'stop':
		break
	elif not reply.isdigit():
		print 'Bad!' * 8
	else:
		print math.sqrt(int(reply))
print 'Bye'
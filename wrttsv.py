from temps.py import read_temp
from threading import Thread
from random import randint
from time import gmtime, strftime, sleep


def wrt_data_tsv():		#write data for tsv
	while (1):
		sleep(10)
		temp = read_temp()
		t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		fop = open("data.tsv","a")
		fop.write(t+"\t"+temp+"\n")
		fop.close()

def Main():
	print "main"
	
	t = Thread(target=wrt_data_tsv)
	t.start()

if __name__ == '__main__':
	Main()

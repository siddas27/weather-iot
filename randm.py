from threading import Thread
from random import randint
from time import gmtime, strftime, sleep

def gen_data(): 		#generate random data
	print "gen"
	while (1):
		sleep(5)
		fop = open("temp.txt","w")
		fop.write(str(randint(15,30)))
		fop.close()

def wrt_data_tsv():		#write data for tsv
	print "tsv"
	while (1):
		sleep(10)
		t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		fo = open("temp.txt","r")
		temp = fo.read()
		fo.close()
		fop = open("data.tsv","a")
		fop.write(t+"\t"+temp+"\n")
		fop.close()

def Main():
	print "main"
	t1 = Thread(target=gen_data)
	t2 = Thread(target=wrt_data_tsv)
	
	t1.start()
	t2.start()
	

if __name__ == '__main__':
	Main()

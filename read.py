def read_temp():		#read temp data
	fof = open("temp.txt","r")
	temp = fof.read()
	fof.close()
	return temp
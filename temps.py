import time
temp_address="/sys/bus/w1/devices/28-03160140daff/w1_slave"

def read_temp():
        file=open(temp_address,"r")
        data=file.read()
        file.close()
        a=data.split()
        b=a[len(a)-1]
        reading=b[2:]
        temp=float(reading)/1000
        time.sleep(1)
        return temp

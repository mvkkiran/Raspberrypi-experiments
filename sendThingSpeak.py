import Adafruit_DHT
 
 

import httplib,urllib,time
from random import randint

apikey = "IM0IX8NXA6ASIKWR"


#https://api.thingspeak.com/update?api_key=IM0IX8NXA6ASIKWR&field1=0

while True:

	humidity, temperature = Adafruit_DHT.read_retry(11, 2)
	hum=humidity
	print hum
	temp=temperature
	print temp
	
	params= urllib.urlencode({'field1':hum,'field2':temp,'key':apikey})
	headers={"Content-type":"application/x-www-form-urlencoded","Accept": "text/plain"}
	conn=httplib.HTTPConnection("api.thingspeak.com:80")

	conn.request("POST","/update",params,headers)
	response=conn.getresponse()
    

        print response.status
	
	conn.close()

	

	time.sleep(10)




import grovepi
from Adafruit_IO import *
ADAFRUIT_IO_USERNAME = "#YOUR_USERNAME"
ADAFRUIT_IO_KEY = "#YOUR_ADAFRUIT_KEY"
aio=Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
relay=3
test=aio.feeds('led')
print(test)
while 1:
     data = aio.receive(test.key)
     print(data.value)
     if data.value=='ON':
          grovepi.digitalWrite(relay,1)
     else:
          grovepi.digitalWrite(relay,0)

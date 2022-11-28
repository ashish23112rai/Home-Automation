import grovepi
from Adafruit_IO import *
ADAFRUIT_IO_USERNAME = "salikmanzer6"
ADAFRUIT_IO_KEY = "aio_XEGK02WqyrYmKbym1jvZQVrHkC0K"
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
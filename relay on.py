import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
print "Relay1 on"
GPIO.output(18,GPIO.HIGH)
print "Relay2 on"
GPIO.output(23,GPIO.HIGH)
print "Relay3 on"
GPIO.output(24,GPIO.HIGH)
print "Relay4 on"
GPIO.output(25,GPIO.HIGH)
print "Relay5 on"
GPIO.output(12,GPIO.HIGH)
print "Relay6 on"
GPIO.output(16,GPIO.HIGH)
print "Relay7 on"
GPIO.output(20,GPIO.HIGH)
print "Relay8 on"
GPIO.output(21,GPIO.HIGH)

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
print "Relay1 off"
GPIO.output(18,GPIO.LOW)
print "Relay2 off"
GPIO.output(23,GPIO.LOW)
print "Relay3 off"
GPIO.output(24,GPIO.LOW)
print "Relay4 off"
GPIO.output(25,GPIO.LOW)
print "Relay5 off"
GPIO.output(12,GPIO.LOW)
print "Relay6 off"
GPIO.output(16,GPIO.LOW)
print "Relay7 off"
GPIO.output(20,GPIO.LOW)
print "Relay8 off"
GPIO.output(21,GPIO.LOW)

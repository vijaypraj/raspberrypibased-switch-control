from flask import Flask, render_template
from RPi import GPIO

app = Flask(__name__)

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

@app.route('/')
def render_index():
    return render_template('index.html')

@app.route('/on/<int:gpio>')
def switch_on(gpio):
    GPIO.output(gpio,GPIO.LOW)
    return True

@app.route('/off/<int:gpio>')
def switch_on(gpio):
    GPIO.output(gpio,GPIO.HIGH)
    return True

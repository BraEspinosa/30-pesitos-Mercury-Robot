#bookstores
import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
#initialization of functions
pins = {
    4 : {'name' : 'Izq15', 'state' : GPIO.LOW},
    17 : {'name' : 'Avanzar', 'state' : GPIO.LOW},
    27 : {'name' : 'Retroceder', 'state' : GPIO.LOW},
    22 : {'name' : 'Izq45', 'state' : GPIO.LOW},
    10 : {'name' : 'Pulso', 'state' : GPIO.LOW},
    9 : {'name' : 'Subiendo', 'state' : GPIO.LOW},
    11 : {'name' : 'Der15', 'state' : GPIO.LOW},
    6 : {'name' : 'Der45', 'state' : GPIO.LOW},
    5 : {'name' : 'LUZ', 'state' : GPIO.LOW}
}
#initialization of pins in use
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.LOW)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.LOW)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, GPIO.LOW)
GPIO.setup(25, GPIO.OUT)
GPIO.output(25, GPIO.LOW)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.LOW)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
izquierda=GPIO.PWM(8,100)
derecha=GPIO.PWM(7,100)
izquierda.start(100)
derecha.start(100)

#bonding between main.html and weblamp.py
@app.route("/")
def main():
    for pin in pins:
        pins[pin]['state'] = GPIO.input(pin)
    templateData = {
        'pins' : pins
        }
    return render_template('main.html', **templateData)

#function protocol
@app.route("/<changePin>/<action>")
def action(changePin, action):
    changePin = int(changePin)
    deviceName = pins[changePin]['name']
    if action == "on":
        if (deviceName=="Avanzar"):
            derecha.ChangeDutyCycle(70)
            izquierda.ChangeDutyCycle(100)
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.HIGH)
            GPIO.output(25,GPIO.LOW)
            GPIO.output(changePin, GPIO.HIGH)
        if (deviceName=="LUZ"):
            GPIO.output(12,GPIO.HIGH)
            GPIO.output(changePin, GPIO.HIGH)
        if (deviceName=="Retroceder"):
            derecha.ChangeDutyCycle(100)
            izquierda.ChangeDutyCycle(78)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.HIGH)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(25,GPIO.HIGH)
            GPIO.output(changePin, GPIO.HIGH)

        if (deviceName=="Izq15"):
            derecha.ChangeDutyCycle(100)
            izquierda.ChangeDutyCycle(100)
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            GPIO.output(changePin, GPIO.HIGH)
        if (deviceName=="Izq45"):
            derecha.ChangeDutyCycle(100)
            izquierda.ChangeDutyCycle(100)
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            GPIO.output(changePin, GPIO.HIGH)
        if (deviceName=="Pulso"):
            derecha.ChangeDutyCycle(70)
            izquierda.ChangeDutyCycle(100)
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.HIGH)
            GPIO.output(25,GPIO.LOW)
            time.sleep(1)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            GPIO.output(changePin, GPIO.HIGH)

        if (deviceName=="Der15"):
            derecha.ChangeDutyCycle(100)
            izquierda.ChangeDutyCycle(100)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.HIGH)
            GPIO.output(25,GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            GPIO.output(changePin, GPIO.HIGH)
        if (deviceName=="Der45"):
            derecha.ChangeDutyCycle(100)
            izquierda.ChangeDutyCycle(100)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.HIGH)
            GPIO.output(25,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            GPIO.output(changePin, GPIO.HIGH)
        if (deviceName=="Subiendo"):
            derecha.ChangeDutyCycle(85)
            izquierda.ChangeDutyCycle(100)
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.HIGH)
            GPIO.output(25,GPIO.LOW)
            GPIO.output(changePin, GPIO.HIGH)

        message = "Turned " + deviceName + " on."
    if action == "off":
        if (deviceName=="Der15"):
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.HIGH)
            GPIO.output(25,GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            GPIO.output(changePin, GPIO.LOW)
        if (deviceName=="Der45"):
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.HIGH)
            GPIO.output(25,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            GPIO.output(changePin, GPIO.LOW)
        if (deviceName=="LUZ"):
            GPIO.output(12,GPIO.LOW)
            GPIO.output(changePin, GPIO.LOW)
        if (deviceName=="Izq15"):
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            GPIO.output(changePin, GPIO.LOW)
        if (deviceName=="Izq45"):
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            GPIO.output(changePin, GPIO.LOW)
        if (deviceName=="Pulso"):
            izquierda.ChangeDutyCycle(100)
            derecha.ChangeDutyCycle(70)
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.HIGH)
            GPIO.output(25,GPIO.LOW)
            time.sleep(1)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            GPIO.output(changePin, GPIO.LOW)

        else:
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
            derecha.ChangeDutyCycle(100)
            izquierda.ChangeDutyCycle(100)
            GPIO.output(changePin, GPIO.LOW)
        message = "Turned " + deviceName + " off."
    if action == "toggle":
        GPIO.output(changePin,not GPIO.input(changePin))
        message = "Toggled " + deviceName + "."

    for pin in pins:
        pins[pin]['state'] = GPIO.input(pin)

    templateData = {
        'message' : message,
        'pins' : pins
    }

    return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)

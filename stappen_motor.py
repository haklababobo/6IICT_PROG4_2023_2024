from time import sleep
import RPi.GPIO as GPIO

# Pinnummers toewijzen
i1 = 8   # Pinnummer voor output i1
i2 = 9   # Pinnummer voor output i2
i3 = 10  # Pinnummer voor output i3
i4 = 11  # Pinnummer voor output i4
sensorPin = 0  # Pinnummer voor de sensor
buttonPin1 = 2 # Pinnummer voor knop 1
buttonPin2 = 3 # Pinnummer voor knop 2

# GPIO initialiseren
GPIO.setmode(GPIO.BCM)
GPIO.setup(i1, GPIO.OUT)
GPIO.setup(i2, GPIO.OUT)
GPIO.setup(i3, GPIO.OUT)
GPIO.setup(i4, GPIO.OUT)
GPIO.setup(buttonPin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonPin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Functie om te draaien
mymotortest.motor_run(GPIOPins, wait, steps, counterclockwise, verbose, steptype, initdelay)

# Hoofdprogramma
try:
    while True:
        # Lees de status van de knoppen en de sensor
        buttonState1 = GPIO.input(buttonPin1)
        buttonState2 = GPIO.input(buttonPin2)
        sensorValue = 0  # Vervang dit door de werkelijke waarde van de sensor

        # Controleer of knop 1 is ingedrukt
        if buttonState1 == GPIO.HIGH:
            # Roteer in de positieve richting
            for j in range(4097):
                stap += 1
                if stap > 7:
                    stap = 0
                draaie(stap)  # Roteer naar de huidige stap
                sleep(sensorValue / 1000000.0)  # Wacht een korte periode

        # Controleer of knop 2 is ingedrukt
        if buttonState2 == GPIO.HIGH:
            # Roteer in de negatieve richting
            for j in range(4097):
                stap -= 1
                if stap < 0:
                    stap = 7
                draaie(stap)  # Roteer naar de huidige stap
                sleep(sensorValue / 1000000.0)  # Wacht een korte periode

except KeyboardInterrupt:
    print("Programma onderbroken")
finally:
    GPIO.cleanup()  # GPIO pinnen schoonmaken bij afsluiten

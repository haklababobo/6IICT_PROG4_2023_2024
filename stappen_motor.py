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
def draaie(stap):
    if stap == 0:
        # Stap 0: zet i1, i2 en i3 laag, i4 hoog
        GPIO.output(i1, GPIO.LOW)
        GPIO.output(i2, GPIO.LOW)
        GPIO.output(i3, GPIO.LOW)
        GPIO.output(i4, GPIO.HIGH)
    elif stap == 1:
        # Stap 1: zet i1 en i2 laag, i3 en i4 hoog
        GPIO.output(i1, GPIO.LOW)
        GPIO.output(i2, GPIO.LOW)
        GPIO.output(i3, GPIO.HIGH)
        GPIO.output(i4, GPIO.HIGH)
    elif stap == 2:
        # Stap 2: zet i1 en i2 laag, i3 laag, i4 hoog
        GPIO.output(i1, GPIO.LOW)
        GPIO.output(i2, GPIO.LOW)
        GPIO.output(i3, GPIO.HIGH)
        GPIO.output(i4, GPIO.LOW)
    elif stap == 3:
        # Stap 3: zet i1 laag, i2 en i3 hoog, i4 laag
        GPIO.output(i1, GPIO.LOW)
        GPIO.output(i2, GPIO.HIGH)
        GPIO.output(i3, GPIO.HIGH)
        GPIO.output(i4, GPIO.LOW)
    elif stap == 4:
        # Stap 4: zet i1 laag, i2 hoog, i3 en i4 laag
        GPIO.output(i1, GPIO.LOW)
        GPIO.output(i2, GPIO.HIGH)
        GPIO.output(i3, GPIO.LOW)
        GPIO.output(i4, GPIO.LOW)
    elif stap == 5:
        # Stap 5: zet i1, i2 hoog, i3 en i4 laag
        GPIO.output(i1, GPIO.HIGH)
        GPIO.output(i2, GPIO.HIGH)
        GPIO.output(i3, GPIO.LOW)
        GPIO.output(i4, GPIO.LOW)
    elif stap == 6:
        # Stap 6: zet i1 hoog, i2 en i3 laag, i4 laag
        GPIO.output(i1, GPIO.HIGH)
        GPIO.output(i2, GPIO.LOW)
        GPIO.output(i3, GPIO.LOW)
        GPIO.output(i4, GPIO.LOW)
    elif stap == 7:
        # Stap 7: zet i1 hoog, i2 laag, i3 en i4 hoog
        GPIO.output(i1, GPIO.HIGH)
        GPIO.output(i2, GPIO.LOW)
        GPIO.output(i4, GPIO.HIGH)
        GPIO.output(i3, GPIO.LOW)
    else:
        # Ongeldige stap: zet alle pinnen laag
        GPIO.output(i1, GPIO.LOW)
        GPIO.output(i2, GPIO.LOW)
        GPIO.output(i3, GPIO.LOW)
        GPIO.output(i4, GPIO.LOW)


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

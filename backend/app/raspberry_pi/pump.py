# TODO use the sensors from rasspberry
# import RPi.GPIO as GPIO
# from app.raspberry_pi.config import PUMP_PIN

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(PUMP_PIN, GPIO.OUT)
# GPIO.output(PUMP_PIN, GPIO.LOW)


def turn_on() -> None:
    print("turn on")
    # GPIO.output(PUMP_PIN, GPIO.HIGH)


def turn_off() -> None:
    print("turn off")
    # GPIO.output(PUMP_PIN, GPIO.LOW)

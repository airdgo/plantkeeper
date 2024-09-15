import RPi.GPIO as GPIO

from app.raspberry_pi.config import PUMP_PIN

GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMP_PIN, GPIO.OUT)
GPIO.output(PUMP_PIN, GPIO.LOW)


def turn_on() -> None:
    GPIO.output(PUMP_PIN, GPIO.HIGH)


def turn_off() -> None:
    GPIO.output(PUMP_PIN, GPIO.LOW)

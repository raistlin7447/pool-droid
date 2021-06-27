from pathlib import Path
from typing import Tuple

from django.contrib import admin
from django.db import models
from w1thermsensor import W1ThermSensor, Unit

try:
    import RPi.GPIO as GPIO
except:
    pass


class Relay(models.Model):
    name = models.CharField(max_length=100, unique=True)
    gpio_bcm = models.PositiveSmallIntegerField(unique=True, help_text="GPIO Port Number")
    initial_state = models.BooleanField(default=False, help_text="State to initialize port to")

    @admin.display(boolean=True, description="Enabled")
    def get_state(self) -> bool:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bcm, GPIO.OUT)
        return bool(GPIO.input(self.gpio_bcm))

    def set_state(self, state: bool) -> bool:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bcm, GPIO.OUT)
        GPIO.output(self.gpio_bcm, state)
        return bool(GPIO.input(self.gpio_bcm))


class OneWireTempSensor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=12, unique=True)

    @admin.display(description="Temp C / Temp F")
    def get_temps(self, digits: int = 1) -> Tuple[float, float]:
        sensor = W1ThermSensor(sensor_id=self.address)
        temp_c, temp_f = sensor.get_temperatures([Unit.DEGREES_C, Unit.DEGREES_F])
        return round(temp_c, digits), round(temp_f, digits)

    def get_temp_c(self, digits: int = 1) -> float:
        return self.get_temps(digits=digits)[0]

    def get_temp_f(self, digits: int = 1) -> float:
        return self.get_temps(digits=digits)[1]

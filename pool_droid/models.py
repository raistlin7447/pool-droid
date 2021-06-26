from django.contrib import admin
from django.db import models
try:
    import RPi.GPIO as GPIO
except:
    pass


class Relay(models.Model):
    name = models.CharField(max_length=100, unique=True)
    gpio_bcm = models.PositiveSmallIntegerField(unique=True, help_text="GPIO Port Number")
    initial_state = models.BooleanField(default=False, help_text="State to initialize port to")

    @admin.display(boolean=True)
    def get_state(self) -> bool:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bcm, GPIO.OUT)
        return bool(GPIO.input(self.gpio_bcm))

    def set_state(self, state: bool) -> bool:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bcm, GPIO.OUT)
        GPIO.output(self.gpio_bcm, state)
        return bool(GPIO.input(self.gpio_bcm))

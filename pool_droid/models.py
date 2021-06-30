from typing import Tuple

import serial
from django.contrib import admin
from django.db import models
from w1thermsensor import W1ThermSensor, Unit

import pypentair

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


class PentairPump(models.Model):
    name = models.CharField(max_length=100, unique=True)
    pump_address = models.CharField(max_length=4, choices=[(hex(v), k) for k, v in pypentair.ADDRESSES.items()])
    port = models.CharField(max_length=100, unique=True)
    baud_rate = models.IntegerField(default=9600, choices=[(i, i) for i in serial.SerialBase.BAUDRATES])
    byte_size = models.FloatField(default=serial.EIGHTBITS, choices=[(i, i) for i in serial.SerialBase.BYTESIZES])
    parity = models.CharField(default=serial.PARITY_NONE, choices=serial.PARITY_NAMES.items(), max_length=1)
    stop_bits = models.FloatField(default=serial.STOPBITS_ONE, choices=[(i, i) for i in serial.SerialBase.STOPBITS])

    def get_pump_connection(self):
        serial_con = serial.Serial(
            port=self.port,
            baudrate=self.baud_rate,
            bytesize=self.byte_size,
            parity=self.parity,
            stopbits=self.stop_bits,
            timeout=1
        )
        return pypentair.Pump(self.pump_address, serial_con)

    @admin.display(description="Current Speed")
    def get_speed(self):
        return self.get_pump_connection().status["rpm"]

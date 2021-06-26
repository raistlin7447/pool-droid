import glob
import os
import time

try:
    from pypentair import Pump
except:
    pass

try:
    import RPi.GPIO as GPIO
except:
    pass

RELAY_TO_GPIO_MAP = {
    1: 22,
    2: 25,
    3: 24,
    4: 23
}


def get_one_wire_temp_probe():
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')
    if device_folder:
        return device_folder[0] + '/w1_slave'
    else:
        return None


def read_temp_raw(device_file):
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def get_cabinet_temp():
    device_file = get_one_wire_temp_probe()

    if device_file:
        lines = read_temp_raw(device_file)
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw(device_file)
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_c, temp_f
    return None, None


def get_pump_speed():
    return Pump(1).status["rpm"]

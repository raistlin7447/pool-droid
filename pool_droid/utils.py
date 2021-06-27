try:
    from pypentair import Pump
except:
    pass

def get_pump_speed():
    return Pump(1).status["rpm"]

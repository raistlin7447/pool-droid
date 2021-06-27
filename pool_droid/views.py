from django.http import HttpResponse
from django.views import View

from pool_droid.models import Relay, OneWireTempSensor
from pool_droid.utils import get_pump_speed


class HomeView(View):
    def get(self, request):
        temp_str = ""
        for sensor in OneWireTempSensor.objects.all():
            temp_str += f"{sensor.name}: {sensor.get_temp_f()} °F, "

        relay_str = ""
        for relay in Relay.objects.all():
            relay_str += f"{relay.name}: {relay.get_state()}, "

        pump_speed = get_pump_speed()
        return HttpResponse(f"{temp_str}{relay_str} Pump Speed: {pump_speed}")

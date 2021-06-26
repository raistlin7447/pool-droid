from django.http import HttpResponse
from django.views import View

from pool_droid.models import Relay
from pool_droid.utils import get_cabinet_temp, get_pump_speed


class HomeView(View):
    def get(self, request):
        temp_c, temp_f = get_cabinet_temp()
        relay_str = ""
        for relay in Relay.objects.all():
            relay_str += f"{relay.name}: {relay.get_state()}, "
        pump_speed = get_pump_speed()
        return HttpResponse(f"Cabinet Temp: {temp_c} °C, {temp_f} °F, {relay_str} Pump Speed: {pump_speed}")

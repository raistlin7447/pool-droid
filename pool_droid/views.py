from django.http import HttpResponse
from django.views import View

from pool_droid.utils import get_cabinet_temp, get_relay_status


class HomeView(View):
    def get(self, request):
        temp_c, temp_f = get_cabinet_temp()
        relay_1 = get_relay_status(1)
        relay_2 = get_relay_status(2)
        relay_3 = get_relay_status(3)
        relay_4 = get_relay_status(4)
        return HttpResponse(f"Cabinet Temp: {temp_c} °C, {temp_f} °F, Relay 1: {relay_1}, Relay 2: {relay_2}, Relay 3: {relay_3}, Relay 4: {relay_4}")
